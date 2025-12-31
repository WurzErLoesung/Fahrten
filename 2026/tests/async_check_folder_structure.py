"""
Prüft ob alle benötigten Dateien vorhanden sind
Führe das auf deinem Computer aus (nicht auf dem Hub):
    python check_structure.py
"""

import os
from pathlib import Path

# Erwartete Struktur
EXPECTED = {
    ".": ["async_color_choose.py", "pupdevices.py", "yaw.py"],
    "brush": ["__init__.py", "async_brush.py"],
    "drive_across": ["__init__.py", "async_drive_across.py"],
    "forum": ["__init__.py", "async_forum.py"],
    "ship": ["__init__.py", "async_ship.py"],
    "stonehenge": ["__init__.py", "async_stonehenge.py"],
    "artifact": ["__init__.py", "async_artifact.py"],
}


def check_structure():
    """Prüft die Ordnerstruktur"""
    base = Path(".")
    all_good = True
    missing = []

    print("=" * 60)
    print("ORDNERSTRUKTUR-PRÜFUNG")
    print("=" * 60)
    print()

    for folder, files in EXPECTED.items():
        folder_path = base / folder
        folder_name = folder if folder != "." else "(Hauptordner)"

        print(f"📁 {folder_name}")

        # Prüfe ob Ordner existiert
        if folder != "." and not folder_path.exists():
            print(f"   ❌ Ordner existiert nicht!")
            all_good = False
            missing.append(f"Ordner: {folder}/")
            print()
            continue

        # Prüfe Dateien
        for file in files:
            file_path = folder_path / file
            if file_path.exists():
                size = file_path.stat().st_size
                if file == "__init__.py":
                    # __init__.py sollte leer sein (0 Bytes OK)
                    print(f"   ✅ {file} ({size} bytes)")
                else:
                    print(f"   ✅ {file} ({size} bytes)")
            else:
                print(f"   ❌ {file} FEHLT!")
                all_good = False
                missing.append(f"{folder}/{file}")

        print()

    print("=" * 60)
    if all_good:
        print("✅ ALLES VORHANDEN!")
        print("=" * 60)
        print("\nDu kannst jetzt auf den Hub laden:")
        print("  pybricksdev run main.py")
    else:
        print("❌ FEHLENDE DATEIEN/ORDNER!")
        print("=" * 60)
        print("\nFolgendes fehlt:")
        for item in missing:
            print(f"  - {item}")

        print("\nWas tun:")
        if any("__init__.py" in item for item in missing):
            print("  1. Erstelle fehlende __init__.py Dateien (leer!)")
            print("     Verwende: python create_init_files.py")
        if any("main.py" in item for item in missing):
            print("  2. Kopiere main.py aus dem Artifact")
        print("  3. Prüfe ob alle Mission-Dateien da sind")
        print("  4. Führe dieses Script nochmal aus")


if __name__ == "__main__":
    try:
        check_structure()
    except Exception as e:
        print(f"\n❌ FEHLER: {e}")
