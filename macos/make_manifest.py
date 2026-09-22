"""Writes (and verifies) the macOS release manifest. Called by macos/release.sh.

Two channels:

* **primary**  - https://claudeusagemonitor.com/macos/  (this is the home of the project)
* **legacy**   - the old address, only so copies installed before the move keep updating.
  Its manifest points the download at the OLD host, because that is what those installs fetch.
  Files: ``<site>/manifest.json`` etc. for primary, ``<site>/legacy/…`` for legacy.

The Windows release is the base of the project: unless --force is given, a macOS release is
refused for a version that is not in the Windows versions.json of the primary site. The notes
are the ones written for the Windows release (release/notes/<version>.json).
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

UA = "ClaudeUsageMonitor-release"


def get_json(url: str):
    req = urllib.request.Request(url + ("&" if "?" in url else "?") + f"t={int(time.time())}",
                                 headers={"User-Agent": UA, "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8-sig"))
    except urllib.error.HTTPError as e:
        if e.code in (403, 404):
            return None
        raise
    except (urllib.error.URLError, ValueError):
        return None


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def vkey(v: str):
    return tuple(int(x) for x in str(v).split(".") if x.isdigit())


def write_channel(site: str, base: str, zip_path: str, version: str, arch: str, commit: str,
                  digest: str, size: int, notes: dict, now: str) -> str:
    """Writes manifest.json + versions.json + CHANGELOG.md of one channel into `site`."""
    mac = base.rstrip("/") + "/macos/"
    url = mac + "versions/" + os.path.basename(zip_path)
    os.makedirs(site, exist_ok=True)
    manifest = {
        "name": "Claude Usage Monitor", "slug": "claude-usage-monitor", "platform": "macos",
        "version": version, "arch": arch, "download_url": url, "sha256": digest, "bytes": size,
        "requires": "macOS 12 or newer", "source_commit": commit,
        "homepage": base, "last_updated": now, "notes": notes,
    }
    json.dump(manifest, open(os.path.join(site, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    old = get_json(mac + "versions.json") or {}
    versions = [v for v in old.get("versions", [])
                if not (v.get("version") == version and v.get("arch") == arch)]
    versions.append({"version": version, "arch": arch, "download_url": url, "sha256": digest,
                     "released": now, "bytes": size, "source_commit": commit})
    versions.sort(key=lambda v: (vkey(v.get("version", "0")), v.get("released", "")), reverse=True)
    json.dump({"slug": "claude-usage-monitor", "platform": "macos",
               "latest": versions[0]["version"], "versions": versions},
              open(os.path.join(site, "versions.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    lines = ["# Claude Usage Monitor for macOS - releases", ""]
    for v in versions:
        lines.append(f"- **{v['version']}** ({v.get('arch', '?')}) - {str(v.get('released', ''))[:10]} - `{v.get('sha256', '')}`")
    lines += ["", "What changed in each version: see ../CHANGELOG.md (the notes are shared with the "
                  "Windows release).", ""]
    open(os.path.join(site, "CHANGELOG.md"), "w", encoding="utf-8").write("\n".join(lines))
    return url


def verify(site: str, base: str, label: str) -> int:
    mac = base.rstrip("/") + "/macos/"
    local = json.load(open(os.path.join(site, "manifest.json"), encoding="utf-8"))
    live = get_json(mac + "manifest.json")
    if not live or live.get("version") != local["version"] or live.get("sha256") != local["sha256"]:
        print(f"ERROR [{label}]: the live manifest does not match what was uploaded:",
              live and live.get("version"))
        return 1
    req = urllib.request.Request(local["download_url"], method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            size = int(r.headers.get("Content-Length") or 0)
    except (urllib.error.URLError, OSError) as e:
        print(f"ERROR [{label}]: the package is not reachable: {e}")
        return 1
    if size != local["bytes"]:
        print(f"ERROR [{label}]: live package size {size} != {local['bytes']}")
        return 1
    print(f"  LIVE OK [{label}]: manifest {live['version']} ({live.get('arch')}), package {size} bytes")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version"); ap.add_argument("--arch"); ap.add_argument("--zip")
    ap.add_argument("--site", required=True); ap.add_argument("--base-url", required=True)
    ap.add_argument("--legacy-base-url", default="")
    ap.add_argument("--commit", default=""); ap.add_argument("--force", action="store_true")
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    base = a.base_url.rstrip("/") + "/"
    legacy = a.legacy_base_url.rstrip("/") + "/" if a.legacy_base_url.strip() else ""

    if a.verify:
        rc = verify(a.site, base, "primary")
        if legacy and os.path.exists(os.path.join(a.site, "legacy", "manifest.json")):
            rc |= verify(os.path.join(a.site, "legacy"), legacy, "legacy")
        return rc

    # the Windows release of this version has to be published first (primary site)
    win = get_json(base + "versions.json") or {}
    published = [v.get("version") for v in win.get("versions", [])]
    if a.version not in published:
        msg = (f"version {a.version} is not published for Windows yet (latest there: {win.get('latest')}). "
               "The Windows release is the base - ask Gabor to release it first")
        if not a.force:
            print("ERROR: " + msg + ", or use --force if he told you to go ahead.")
            return 1
        print("  WARNING: " + msg + " - continuing because of --force.")

    notes = {"en": [], "hu": []}
    notes_file = os.path.join("release", "notes", f"{a.version}.json")
    if os.path.exists(notes_file):
        notes.update(json.load(open(notes_file, encoding="utf-8")))

    size = os.path.getsize(a.zip)
    digest = sha256(a.zip)
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    url = write_channel(a.site, base, a.zip, a.version, a.arch, a.commit, digest, size, notes, now)
    print(f"  primary: {url}")
    if legacy:
        lurl = write_channel(os.path.join(a.site, "legacy"), legacy, a.zip, a.version, a.arch,
                             a.commit, digest, size, notes, now)
        print(f"  legacy:  {lurl}")
    print(f"  sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
