"""Writes (and verifies) the macOS release manifest. Called by macos/release.sh.

The Windows release is the base of the project: unless --force is given, a macOS release is
refused for a version that is not in the Windows versions.json on the server. The notes are
the ones written for the Windows release (release/notes/<version>.json).
"""
import argparse
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request


def get_json(url: str):
    req = urllib.request.Request(url + ("&" if "?" in url else "?") + f"t={int(time.time())}",
                                 headers={"User-Agent": "ClaudeUsageMonitor-release", "Cache-Control": "no-cache"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode("utf-8-sig"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def vkey(v: str):
    return tuple(int(x) for x in v.split(".") if x.isdigit())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--version"); ap.add_argument("--arch"); ap.add_argument("--zip")
    ap.add_argument("--site", required=True); ap.add_argument("--base-url", required=True)
    ap.add_argument("--commit", default=""); ap.add_argument("--force", action="store_true")
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    base = a.base_url.rstrip("/") + "/"
    mac = base + "macos/"
    manifest_path = os.path.join(a.site, "manifest.json")

    if a.verify:
        local = json.load(open(manifest_path, encoding="utf-8"))
        live = get_json(mac + "manifest.json")
        if not live or live.get("version") != local["version"] or live.get("sha256") != local["sha256"]:
            print("ERROR: the live manifest does not match what was uploaded:", live and live.get("version"))
            return 1
        req = urllib.request.Request(local["download_url"], method="HEAD", headers={"User-Agent": "ClaudeUsageMonitor-release"})
        with urllib.request.urlopen(req, timeout=60) as r:
            size = int(r.headers.get("Content-Length") or 0)
        if size != local["bytes"]:
            print(f"ERROR: live package size {size} != {local['bytes']}")
            return 1
        print(f"  LIVE OK: macOS manifest {live['version']} ({live.get('arch')}), package {size} bytes")
        return 0

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
    url = mac + "versions/" + os.path.basename(a.zip)
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    manifest = {
        "name": "Claude Usage Monitor", "slug": "claude-usage-monitor", "platform": "macos",
        "version": a.version, "arch": a.arch, "download_url": url, "sha256": digest, "bytes": size,
        "requires": "macOS 12 or newer", "source_commit": a.commit,
        "homepage": base, "last_updated": now, "notes": notes,
    }
    json.dump(manifest, open(manifest_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    old = get_json(mac + "versions.json") or {}
    versions = [v for v in old.get("versions", []) if not (v.get("version") == a.version and v.get("arch") == a.arch)]
    versions.append({"version": a.version, "arch": a.arch, "download_url": url, "sha256": digest,
                     "released": now, "bytes": size, "source_commit": a.commit})
    versions.sort(key=lambda v: vkey(v["version"]), reverse=True)
    json.dump({"slug": "claude-usage-monitor", "platform": "macos", "latest": versions[0]["version"], "versions": versions},
              open(os.path.join(a.site, "versions.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    lines = [f"# Claude Usage Monitor for macOS - releases", ""]
    for v in versions:
        lines.append(f"- **{v['version']}** ({v['arch']}) - {v['released'][:10]} - `{v['sha256']}`")
    lines += ["", "What changed in each version: see ../CHANGELOG.md (the notes are shared with the Windows release).", ""]
    open(os.path.join(a.site, "CHANGELOG.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"  sha256 {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
