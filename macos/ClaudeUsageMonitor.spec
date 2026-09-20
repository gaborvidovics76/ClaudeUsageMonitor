# PyInstaller spec for the macOS .app bundle.  Used by macos/build.sh - do not run it by hand.
# -*- mode: python ; coding: utf-8 -*-
import os

ROOT = os.path.abspath(os.path.join(SPECPATH, ".."))
VERSION = os.environ.get("UM_VERSION", "0.0.0")

EXCLUDES = [
    "PySide6.QtWebEngineCore", "PySide6.QtWebEngineWidgets", "PySide6.QtWebEngineQuick",
    "PySide6.QtWebChannel", "PySide6.QtQml", "PySide6.QtQuick", "PySide6.QtQuick3D",
    "PySide6.QtQuickWidgets", "PySide6.Qt3DCore", "PySide6.QtMultimedia", "PySide6.QtSql",
    "PySide6.QtTest", "PySide6.QtPdf", "PySide6.QtOpenGL", "PySide6.QtCharts",
    "PySide6.QtDataVisualization", "tkinter", "unittest", "pydoc",
]

a = Analysis(
    [os.path.join(ROOT, "main.py")],
    pathex=[ROOT],
    hiddenimports=["keyring.backends.macOS"],     # the Keychain backend is chosen by hand when frozen
    excludes=EXCLUDES,
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz, a.scripts, [],
    exclude_binaries=True,
    name="ClaudeUsageMonitor",
    console=False,
    target_arch=None,                 # the architecture of the Mac that builds
)
coll = COLLECT(exe, a.binaries, a.datas, name="ClaudeUsageMonitor")
app = BUNDLE(
    coll,
    name="ClaudeUsageMonitor.app",
    icon=os.path.join(ROOT, "build-macos", "app.icns"),
    bundle_identifier="hu.dinorr.claudeusagemonitor",
    version=VERSION,
    info_plist={
        "CFBundleName": "Claude Usage Monitor",
        "CFBundleDisplayName": "Claude Usage Monitor",
        "CFBundleShortVersionString": VERSION,
        "CFBundleVersion": VERSION,
        "LSUIElement": True,              # a panel + menu bar icon: no Dock icon, no app menu
        "LSMinimumSystemVersion": "12.0",
        "NSHighResolutionCapable": True,
        "NSHumanReadableCopyright": "MIT licence - unofficial community tool, not affiliated with Anthropic",
    },
)
