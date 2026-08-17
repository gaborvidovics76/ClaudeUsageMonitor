"""Windows-specifikus apróságok: automatikus indítás, ikonkészítés."""

from __future__ import annotations

import os
import sys
from typing import Optional

from PySide6.QtCore import QBuffer, QByteArray, QIODevice, QRectF, Qt
from PySide6.QtGui import QColor, QFont, QIcon, QPainter, QPainterPath, QPixmap

RUN_KEY = r"Software\Microsoft\Windows\CurrentVersion\Run"
RUN_VALUE = "ClaudeUsageMonitor"
TASK_NAME = "ClaudeUsageMonitor"

# A Run kulcs bejelentkezéskor néha egyszerűen nem fut le (AV-ellenőrzés, korai
# indulás, a Windows "startup impact" szabályozása). Az ütemezett feladat
# megbízhatóbb, és késleltetést is tud, ezért az az elsődleges módszer.

TASK_XML = """<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Description>Claude Usage Monitor indítása bejelentkezéskor</Description>
    <URI>\\{name}</URI>
  </RegistrationInfo>
  <Triggers>
    <LogonTrigger>
      <Enabled>true</Enabled>
      <UserId>{user}</UserId>
      <Delay>PT20S</Delay>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>{user}</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>false</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>7</Priority>
    <RestartOnFailure>
      <Interval>PT1M</Interval>
      <Count>3</Count>
    </RestartOnFailure>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>{command}</Command>
      <WorkingDirectory>{workdir}</WorkingDirectory>
    </Exec>
  </Actions>
</Task>
"""


def launch_command() -> str:
    if getattr(sys, "frozen", False):
        return f'"{sys.executable}"'
    script = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "main.py"))
    exe = sys.executable.replace("python.exe", "pythonw.exe")
    return f'"{exe}" "{script}"'


def _run_hidden(args: list) -> "subprocess.CompletedProcess":
    import subprocess

    return subprocess.run(
        args,
        capture_output=True,
        text=True,
        encoding="oem",
        errors="replace",
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )


def exe_path() -> str:
    """Az indítandó fájl (fagyasztva az exe, fejlesztéskor a pythonw)."""
    if getattr(sys, "frozen", False):
        return sys.executable
    return sys.executable.replace("python.exe", "pythonw.exe")


# ------------------------------------------------- Start menü parancsikon

START_MENU_NAME = "Claude Usage Monitor"


def start_menu_path() -> str:
    appdata = os.environ.get("APPDATA") or os.path.expanduser("~\\AppData\\Roaming")
    return os.path.join(appdata, "Microsoft", "Windows", "Start Menu",
                        "Programs", START_MENU_NAME + ".lnk")


def start_menu_exists() -> bool:
    return os.path.exists(start_menu_path())


def create_start_menu_shortcut() -> bool:
    """Parancsikon a Start menübe (WScript.Shell COM-on át, PowerShell segéddel)."""
    target = exe_path()
    lnk = start_menu_path()
    workdir = os.path.dirname(target)
    ps = (
        "$w = New-Object -ComObject WScript.Shell; "
        f"$s = $w.CreateShortcut('{lnk}'); "
        f"$s.TargetPath = '{target}'; "
        f"$s.WorkingDirectory = '{workdir}'; "
        f"$s.IconLocation = '{target},0'; "
        "$s.Description = 'Claude Usage Monitor'; "
        "$s.Save()"
    )
    try:
        os.makedirs(os.path.dirname(lnk), exist_ok=True)
        res = _run_hidden(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps])
        return res.returncode == 0 and start_menu_exists()
    except OSError:
        return False


def remove_start_menu_shortcut() -> None:
    try:
        os.remove(start_menu_path())
    except OSError:
        pass


def ensure_start_menu_shortcut() -> None:
    """Csak a csomagolt exe-nél, és csak ha még nincs – így nem tolakodó."""
    if getattr(sys, "frozen", False) and not start_menu_exists():
        create_start_menu_shortcut()


# ------------------------------------------------- ütemezett feladat (elsődleges)


def task_command() -> Optional[str]:
    """A feladathoz bejegyzett futtatandó parancs, vagy None, ha nincs feladat."""
    res = _run_hidden(["schtasks", "/Query", "/TN", TASK_NAME, "/XML"])
    if res.returncode != 0 or not res.stdout:
        return None
    import re

    m = re.search(r"<Command>(.*?)</Command>", res.stdout, re.S)
    return m.group(1).strip() if m else ""


def set_task_autostart(enabled: bool) -> bool:
    import os
    import tempfile

    if not enabled:
        res = _run_hidden(["schtasks", "/Delete", "/TN", TASK_NAME, "/F"])
        return res.returncode == 0 or task_command() is None

    command = exe_path()
    if not getattr(sys, "frozen", False):
        # Fejlesztéskor a main.py-t kell átadni argumentumként – a Task Scheduler
        # <Arguments> nélkül nem tudná, mit indítson, ezért ilyenkor a Run kulcs marad.
        return False

    user = os.environ.get("USERNAME", "")
    domain = os.environ.get("USERDOMAIN", "")
    xml = TASK_XML.format(
        name=TASK_NAME,
        user=f"{domain}\\{user}" if domain else user,
        command=command,
        workdir=os.path.dirname(command),
    )
    path = os.path.join(tempfile.gettempdir(), "cum_task.xml")
    with open(path, "w", encoding="utf-16") as fh:
        fh.write(xml)
    try:
        res = _run_hidden(["schtasks", "/Create", "/TN", TASK_NAME, "/XML", path, "/F"])
        return res.returncode == 0
    finally:
        try:
            os.remove(path)
        except OSError:
            pass


# ------------------------------------------------------- Run kulcs (tartalék)


def autostart_command() -> Optional[str]:
    """A jelenleg beregisztrált indítóparancs, vagy None."""
    try:
        import winreg

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_KEY) as key:
            value, _ = winreg.QueryValueEx(key, RUN_VALUE)
            return str(value) or None
    except (ImportError, OSError):
        return None


def set_run_key(enabled: bool) -> bool:
    try:
        import winreg

        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, RUN_KEY, 0, winreg.KEY_SET_VALUE) as key:
            if enabled:
                winreg.SetValueEx(key, RUN_VALUE, 0, winreg.REG_SZ, launch_command())
            else:
                try:
                    winreg.DeleteValue(key, RUN_VALUE)
                except FileNotFoundError:
                    pass
        return True
    except (ImportError, OSError):
        return False


# ------------------------------------------------------------ közös felület


def autostart_method() -> str:
    """'task', 'run' vagy '' (nincs bekapcsolva)."""
    if task_command() is not None:
        return "task"
    if autostart_command() is not None:
        return "run"
    return ""


def autostart_enabled() -> bool:
    return bool(autostart_method())


def set_autostart(enabled: bool) -> bool:
    """Bekapcsoláskor elsődlegesen ütemezett feladat, tartalékként Run kulcs.
    Kikapcsoláskor mindkettőt eltávolítjuk."""
    if not enabled:
        ok_task = set_task_autostart(False)
        ok_run = set_run_key(False)
        return ok_task and ok_run

    if set_task_autostart(True):
        set_run_key(False)          # ne induljon el kétszer
        return True
    return set_run_key(True)


def sync_autostart() -> bool:
    """Ha be van kapcsolva, de elavult útvonalra mutat (áthelyezett vagy
    átnevezett exe), frissítjük a bejegyzést."""
    method = autostart_method()
    if not method:
        return False
    if method == "task":
        if (task_command() or "").strip().lower() != exe_path().strip().lower():
            set_autostart(True)
    else:
        if (autostart_command() or "").strip().lower() != launch_command().strip().lower():
            set_autostart(True)
    return True


# ------------------------------------------------------------------ ikonok


def app_pixmap(size: int = 256, accent: str = "#D97757") -> QPixmap:
    """Az alkalmazás logója: lekerekített négyzet egy csillag-szikrával."""
    pm = QPixmap(size, size)
    pm.fill(Qt.GlobalColor.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.Antialiasing, True)

    path = QPainterPath()
    path.addRoundedRect(QRectF(0, 0, size, size), size * 0.24, size * 0.24)
    p.fillPath(path, QColor(accent))

    p.setPen(Qt.PenStyle.NoPen)
    p.setBrush(QColor(255, 255, 255, 235))
    c, r = size / 2, size * 0.34
    spark = QPainterPath()
    spark.moveTo(c, c - r)
    for i in range(1, 8):
        ang = i * 45
        rad = r if i % 2 == 0 else r * 0.30
        import math

        spark.lineTo(c + rad * math.sin(math.radians(ang)), c - rad * math.cos(math.radians(ang)))
    spark.closeSubpath()
    p.drawPath(spark)
    p.end()
    return pm


def tray_pixmap(value: float, color: QColor, bg: Optional[QColor] = None, size: int = 64) -> QPixmap:
    """Tálcaikon: a százalék nagy számmal; nagyobb méretben körgyűrűvel is."""
    from PySide6.QtGui import QFontMetrics

    pm = QPixmap(size, size)
    pm.fill(Qt.GlobalColor.transparent)
    p = QPainter(pm)
    p.setRenderHint(QPainter.RenderHint.Antialiasing, True)

    if bg is not None:
        path = QPainterPath()
        path.addRoundedRect(QRectF(1, 1, size - 2, size - 2), size * 0.24, size * 0.24)
        p.fillPath(path, bg)

    compact = size <= 28          # a Windows tálca általában 16-24 px-en rajzol
    if not compact:
        pen = p.pen()
        pen.setColor(QColor(color.red(), color.green(), color.blue(), 70))
        pen.setWidthF(size * 0.09)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        p.setPen(pen)
        box = QRectF(size * 0.08, size * 0.08, size * 0.84, size * 0.84)
        p.drawArc(box, 90 * 16, -360 * 16)
        pen.setColor(color)
        p.setPen(pen)
        p.drawArc(box, 90 * 16, int(-360 * 16 * max(0.0, min(1.0, value / 100.0))))

    text = "!" if value >= 99.5 else f"{value:.0f}"
    f = QFont("Segoe UI")
    f.setWeight(QFont.Weight.Bold)
    px = int(size * (0.98 if compact else 0.44))
    limit = size * (1.0 if compact else 0.62)
    while px > 5:
        f.setPixelSize(px)
        if QFontMetrics(f).horizontalAdvance(text) <= limit:
            break
        px -= 1
    p.setFont(f)
    p.setPen(color)
    p.drawText(pm.rect(), Qt.AlignmentFlag.AlignCenter, text)
    p.end()
    return pm


def tray_icon(value: float, color: QColor) -> QIcon:
    icon = QIcon()
    for s in (16, 20, 24, 32, 48, 64):
        icon.addPixmap(tray_pixmap(value, color, size=s))
    return icon


def app_icon(accent: str = "#D97757") -> QIcon:
    icon = QIcon()
    for s in (16, 24, 32, 48, 64, 128, 256):
        icon.addPixmap(app_pixmap(s, accent))
    return icon


def write_ico(path: str, accent: str = "#D97757") -> str:
    """ICO fájl írása PyInstaller számára (beágyazott PNG-kkel)."""
    import struct

    sizes = [16, 24, 32, 48, 64, 128, 256]
    images = []
    for s in sizes:
        ba = QByteArray()
        buf = QBuffer(ba)
        buf.open(QIODevice.OpenModeFlag.WriteOnly)
        app_pixmap(s, accent).save(buf, "PNG")
        buf.close()
        images.append((s, bytes(ba.data())))

    offset = 6 + 16 * len(images)
    header = struct.pack("<HHH", 0, 1, len(images))
    entries, blobs = b"", b""
    for s, data in images:
        entries += struct.pack("<BBBBHHII", s % 256, s % 256, 0, 0, 1, 32, len(data), offset)
        blobs += data
        offset += len(data)
    with open(path, "wb") as fh:
        fh.write(header + entries + blobs)
    return path
