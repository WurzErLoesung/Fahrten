"""
DEBUG-VERSION von main.py
Zeigt genau welche Imports fehlschlagen und warum
"""

from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import StopWatch, run_task, wait

from pupdevices import PupDevices

hub = PrimeHub()
pd = PupDevices()

print(f"\n{'='*40}")
print(f"System: {hub.system.name()}")
print(f"Batterie: {hub.battery.voltage()} mV")
print(f"{'='*40}\n")

print("IMPORT DEBUG - Prüfe alle Module:\n")

# Brush
print("1. Versuche: from brush_new.brush_async import brush_new")
try:
    from brush_new.brush_async import brush_new

    print("   ✅ ERFOLG: brush_new importiert")
    BRUSH = brush_new
except ImportError as e:
    print(f"   ❌ FEHLER: {e}")
    BRUSH = None
except Exception as e:
    print(f"   ❌ ANDERER FEHLER: {type(e).__name__}: {e}")
    BRUSH = None

# Drive Across
print("\n2. Versuche: from drive_across_new.drive_across_new import drive_across_new")
try:
    from drive_across_new.drive_across_new import drive_across_new

    print("   ✅ ERFOLG: drive_across_new importiert")
    DRIVE = drive_across_new
except ImportError as e:
    print(f"   ❌ FEHLER: {e}")
    DRIVE = None
except Exception as e:
    print(f"   ❌ ANDERER FEHLER: {type(e).__name__}: {e}")
    DRIVE = None

# Forum
print("\n3. Versuche: from forum_new.forum_new_new import forum_new_new")
try:
    from forum_new.forum_new_new import forum_new_new

    print("   ✅ ERFOLG: forum_new_new importiert")
    FORUM = forum_new_new
except ImportError as e:
    print(f"   ❌ FEHLER: {e}")
    FORUM = None
except Exception as e:
    print(f"   ❌ ANDERER FEHLER: {type(e).__name__}: {e}")
    FORUM = None

# Ship
print("\n4. Versuche: from ship.ship import ship")
try:
    from ship.ship import ship

    print("   ✅ ERFOLG: ship importiert")
    SHIP = ship
except ImportError as e:
    print(f"   ❌ FEHLER: {e}")
    SHIP = None
except Exception as e:
    print(f"   ❌ ANDERER FEHLER: {type(e).__name__}: {e}")
    SHIP = None

# Stonehenge
print("\n5. Versuche: from stonehenge.stonehenge import stonehenge")
try:
    from stonehenge.stonehenge import stonehenge

    print("   ✅ ERFOLG: stonehenge importiert")
    STONEHENGE = stonehenge
except ImportError as e:
    print(f"   ❌ FEHLER: {e}")
    STONEHENGE = None
except Exception as e:
    print(f"   ❌ ANDERER FEHLER: {type(e).__name__}: {e}")
    STONEHENGE = None

# Trolley
print("\n6. Versuche: from trolley.trolley import trolley")
try:
    from trolley.trolley import trolley

    print("   ✅ ERFOLG: trolley importiert")
    TROLLEY = trolley
except ImportError as e:
    print(f"   ❌ FEHLER: {e}")
    TROLLEY = None
except Exception as e:
    print(f"   ❌ ANDERER FEHLER: {type(e).__name__}: {e}")
    TROLLEY = None

print(f"\n{'='*40}")
print("ZUSAMMENFASSUNG:")
print(f"{'='*40}")
erfolg = sum(
    [1 for x in [BRUSH, DRIVE, FORUM, SHIP, STONEHENGE, TROLLEY] if x is not None]
)
print(f"{erfolg}/6 Module erfolgreich importiert")
print(f"{'='*40}\n")

if erfolg == 0:
    print("❌ KEIN MODUL KONNTE IMPORTIERT WERDEN!")
    print("\nMögliche Ursachen:")
    print("1. __init__.py Dateien fehlen in Unterordnern")
    print("2. Ordnerstruktur stimmt nicht")
    print("3. Dateien sind nicht auf dem Hub")
    print("\nPrüfe:")
    print("  - Existiert brush_new/__init__.py ?")
    print("  - Existiert brush_new/brush_async.py ?")
    print("  - Sind alle Ordner auf dem Hub?")
elif erfolg < 6:
    print(f"⚠️  Nur {erfolg}/6 Module verfügbar")
    print("Prüfe die fehlgeschlagenen Imports oben")
else:
    print("✅ Alle Module erfolgreich importiert!")
    print("Du kannst jetzt das normale main.py verwenden")

print("\nProgramm beendet (Debugging abgeschlossen)")
