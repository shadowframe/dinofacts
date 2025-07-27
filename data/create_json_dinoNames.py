import json

# Lade die bestehende Datei
with open("dino.json", "r", encoding="utf-8") as f:
    dinosaurs = json.load(f)

# Extrahiere nur Namen und ID
# Wir nehmen an, dass jeder Eintrag ein Dict mit "id" und "name" enthält
filtered_dinosaurs = []
for dino in dinosaurs:
    filtered_dinosaurs.append({
        "id": dino.get("id"),
        "name": dino.get("name")
    })

# Speichere in neuer Datei
with open("dino_names.json", "w", encoding="utf-8") as f:
    json.dump(filtered_dinosaurs, f, indent=2, ensure_ascii=False)

print("Datei 'dino_names.json' wurde erfolgreich erstellt.")