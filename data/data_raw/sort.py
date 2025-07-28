import json

# Pfad zur JSON-Datei
input_file = "combined_dinosaurs.json"
output_file = "combined_dinosaurs_sorted.json"

# JSON-Datei laden
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Sortieren nach 'id'
sorted_data = sorted(data, key=lambda x: x.get("id", 0))

# In eine neue Datei speichern (oder gleiche Datei überschreiben)
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(sorted_data, f, indent=2, ensure_ascii=False)

print(f"Die Datei wurde erfolgreich nach ID sortiert gespeichert als: {output_file}")
