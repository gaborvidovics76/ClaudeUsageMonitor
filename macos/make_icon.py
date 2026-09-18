"""Renders the app icon with Qt and turns it into an .icns with the system's iconutil.
Usage: python macos/make_icon.py build-macos/app.icns"""
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PySide6.QtWidgets import QApplication  # noqa: E402

from claude_usage.winutil import app_pixmap  # noqa: E402  (plain Qt drawing, shared by both systems)


def main(out: str) -> int:
    app = QApplication.instance() or QApplication(sys.argv)   # noqa: F841 - Qt needs it for painting
    iconset = os.path.splitext(out)[0] + ".iconset"
    shutil.rmtree(iconset, ignore_errors=True)
    os.makedirs(iconset)
    for size in (16, 32, 128, 256, 512):
        app_pixmap(size).save(os.path.join(iconset, f"icon_{size}x{size}.png"), "PNG")
        app_pixmap(size * 2).save(os.path.join(iconset, f"icon_{size}x{size}@2x.png"), "PNG")
    res = subprocess.run(["/usr/bin/iconutil", "-c", "icns", iconset, "-o", out])
    shutil.rmtree(iconset, ignore_errors=True)
    return res.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "build-macos/app.icns"))
