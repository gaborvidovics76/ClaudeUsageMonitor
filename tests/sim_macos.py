"""Run:  python tests/sim_macos.py   (works on any system)

Exercise the macOS code paths by pretending to be darwin.
What this cannot prove: Qt window behaviour, the real Keychain, ditto, LaunchAgents being honoured."""
import os, plistlib, shutil, sys, tempfile, types, zipfile

tmp = tempfile.mkdtemp(prefix="macsim_")
os.environ["HOME"] = tmp; os.environ["USERPROFILE"] = tmp
import urllib.request  # noqa - real macOS has _scproxy; load it before pretending
sys.platform = "darwin"                       # BEFORE importing the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from claude_usage import settings, datasource
cfg = settings.config_dir()
print("config dir :", cfg.replace(tmp, "~"))
assert cfg.endswith(os.path.join("Library", "Application Support", "ClaudeUsageMonitor")) and os.path.isdir(cfg)
print("desktop log:", datasource.default_data_path().replace(tmp, "~"))
assert os.path.join("Application Support", "Claude", "plan-usage-history.json") in datasource.default_data_path()

# ---- autostart = LaunchAgent plist
from claude_usage import winutil, macutil
assert winutil.set_autostart is macutil.set_autostart and winutil.open_path is macutil.open_path
assert not winutil.autostart_enabled() and winutil.autostart_method() == ""
assert winutil.set_autostart(True) and winutil.autostart_enabled() and winutil.autostart_method() == "launchagent"
pl = plistlib.load(open(macutil.agent_path(), "rb"))
print("LaunchAgent:", {k: pl[k] for k in ("Label", "RunAtLoad", "ProcessType")}, "| args:", len(pl["ProgramArguments"]))
assert pl["Label"] == "hu.dinorr.claudeusagemonitor" and pl["RunAtLoad"] is True
pl["ProgramArguments"] = ["/old/place/ClaudeUsageMonitor"]; plistlib.dump(pl, open(macutil.agent_path(), "wb"))
assert winutil.sync_autostart() and plistlib.load(open(macutil.agent_path(), "rb"))["ProgramArguments"] == macutil.launch_arguments()
assert winutil.set_autostart(False) and not winutil.autostart_enabled()
assert winutil.start_menu_exists() is False and winutil.create_start_menu_shortcut() is False
winutil.ensure_start_menu_shortcut(); winutil.sync_installed_version("9.9.9")
print("autostart on/off/self-heal + no-op Start menu: ok")

# ---- bundle path detection
sys.frozen = True; real_exe = sys.executable
sys.executable = os.path.join(os.sep, "Applications", "ClaudeUsageMonitor.app", "Contents", "MacOS", "ClaudeUsageMonitor")
from claude_usage import updater, updater_mac
bundle = updater.install_dir()
print("bundle     :", bundle); assert bundle.endswith("ClaudeUsageMonitor.app") and macutil.app_bundle_path() == bundle
sys.executable = os.path.join(os.sep, "private", "var", "folders", "x", "AppTranslocation", "ABC", "d", "ClaudeUsageMonitor.app", "Contents", "MacOS", "ClaudeUsageMonitor")
assert updater.can_self_update() == (False, "readonly"); print("App Translocation detected -> manual update offered")
del sys.frozen; sys.executable = real_exe
assert updater.DEFAULT_MANIFEST_URL.endswith("/macos/manifest.json")

# ---- arch rule
import platform
I = updater.UpdateInfo
for machine, arch, want in (("arm64", "arm64", True), ("arm64", "x86_64", True), ("x86_64", "arm64", False),
                            ("x86_64", "x86_64", True), ("x86_64", "", True), ("arm64", "universal2", True)):
    platform.machine = lambda m=machine: m
    assert updater.arch_ok(I("1.0.0", "https://x/y.zip", "0" * 64, arch=arch)) is want, (machine, arch)
print("arch rule (arm64 build never offered to an Intel Mac): ok")

# ---- stage(): simulate ditto by unzipping; symlink/exec-bit fidelity is ditto's job on the real Mac
pkg = os.path.join(tmp, "pkg.zip")
with zipfile.ZipFile(pkg, "w") as z:
    z.writestr("ClaudeUsageMonitor.app/Contents/MacOS/ClaudeUsageMonitor", "bin")
    z.writestr("ClaudeUsageMonitor.app/Contents/Info.plist", "<plist/>")
    z.writestr("READ-ME.txt", "hi")
import subprocess
real_run = subprocess.run
def fake_run(args, **kw):
    if args[0] == "/usr/bin/ditto":
        zipfile.ZipFile(args[3]).extractall(args[4]); return types.SimpleNamespace(returncode=0, stdout="", stderr="")
    return real_run(args, **kw)
updater_mac.subprocess.run = fake_run
apps = os.path.join(tmp, "Applications"); os.makedirs(apps)
staged = updater.stage(pkg, os.path.join(apps, "ClaudeUsageMonitor.app.new"))
assert os.path.isfile(os.path.join(staged, "Contents", "MacOS", "ClaudeUsageMonitor"))
assert [n for n in os.listdir(apps)] == ["ClaudeUsageMonitor.app.new"], os.listdir(apps)      # temp dir cleaned up
bad = os.path.join(tmp, "bad.zip")
with zipfile.ZipFile(bad, "w") as z: z.writestr("../evil.txt", "x")
for label, path in (("path traversal", bad),):
    try: updater.stage(path, os.path.join(apps, "x.app.new")); sys.exit("NOT REJECTED " + label)
    except updater.UpdateError as e: print(f"rejected [{label}]: {e}")
empty = os.path.join(tmp, "empty.zip")
with zipfile.ZipFile(empty, "w") as z: z.writestr("something.txt", "x")
try: updater.stage(empty, os.path.join(apps, "y.app.new")); sys.exit("NOT REJECTED incomplete")
except updater.UpdateError as e: print(f"rejected [no app inside]: {e}")

# ---- Keychain layer: keyring missing -> `security` CLI; never a file
from claude_usage import secretstore, secretstore_mac
assert secretstore.save_secret is secretstore_mac.save_secret
store = {}
def fake_security(args, **kw):
    cmd = args[1]
    if cmd == "add-generic-password": store["v"] = args[args.index("-w") + 1]; return types.SimpleNamespace(returncode=0, stdout="", stderr="")
    if cmd == "find-generic-password": return types.SimpleNamespace(returncode=0 if "v" in store else 44, stdout=store.get("v", "") + "\n", stderr="")
    if cmd == "delete-generic-password": store.pop("v", None); return types.SimpleNamespace(returncode=0, stdout="", stderr="")
secretstore_mac.subprocess.run = fake_security
secretstore_mac._keyring = lambda: None
assert secretstore.load_tokens() is None
assert secretstore.save_tokens({"access_token": "a", "refresh_token": "r"}) and secretstore.load_tokens()["refresh_token"] == "r"
secretstore.clear_secret(); assert secretstore.load_tokens() is None
assert not any(f.endswith(".bin") for f in os.listdir(cfg)), "no token file may be written on macOS"
print("token store -> Keychain layer (no file on disk): ok")

# ---- the rest of the app imports and builds a panel under 'darwin'
from PySide6.QtWidgets import QApplication
app = QApplication([])
from claude_usage import app as appmod, backups, i18n
assert backups.query_tasks("Backup*") == []
print("system language:", i18n.system_language())
from claude_usage.widget import UsageWidget
from claude_usage.datasource import Metrics
s = settings.Settings(); s.save = lambda: None; s["visible"] = False
w = UsageWidget(s); m = Metrics(); m.ok = True; w.set_metrics(m)
from PySide6.QtCore import Qt
assert w.testAttribute(Qt.WidgetAttribute.WA_MacAlwaysShowToolWindow)
print("panel builds with the macOS window attribute: ok")
shutil.rmtree(tmp, ignore_errors=True)
print("MAC SIMULATION OK")
