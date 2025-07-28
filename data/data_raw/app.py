import json
import os

# Pfad zum Arbeitsverzeichnis
verzeichnis = "./"

# Alle relevanten Dateien (die mit 'response' beginnen und auf .json enden)
dateien = sorted([f for f in os.listdir(verzeichnis) if f.startswith("response") and f.endswith(".json")])

# Gesamtliste aller Dinosaurier-Einträge
alle_daten = []

for datei in dateien:
    with open(os.path.join(verzeichnis, datei), "r", encoding="utf-8") as f:
        inhalt = json.load(f)
        daten = inhalt.get("data", [])
        alle_daten.extend(daten)

# Ausgabe in eine neue JSON-Datei
with open("combined_dinosaurs.json", "w", encoding="utf-8") as f_out:
    json.dump(alle_daten, f_out, ensure_ascii=False, indent=2)

print(f"Fertig! {len(alle_daten)} Einträge wurden in 'combined_dinosaurs.json' gespeichert.")
