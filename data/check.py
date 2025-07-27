# prüft ob aufsteigende und lückenlose IDs in einer JSON-Datei vorhanden sind
import json

def check_ids_in_sequence(json_file):
    try:
        # JSON-Datei laden
        with open(json_file, 'r') as file:
            data = json.load(file)
        
        # IDs extrahieren
        ids = [item['id'] for item in data]
        
        # Überprüfen, ob IDs aufsteigend und lückenlos sind
        for i in range(min(ids), max(ids) + 1):
            if i not in ids:
                print(f"Fehlende ID: {i}")
                return False
        
        print("Alle IDs sind aufsteigend und lückenlos vorhanden.")
        return True

    except FileNotFoundError:
        print(f"Die Datei {json_file} wurde nicht gefunden.")
    except json.JSONDecodeError:
        print("Fehler beim Lesen der JSON-Datei. Bitte überprüfen Sie das Format.")
    except KeyError:
        print("Die JSON-Daten enthalten keine 'id'-Felder.")
    except Exception as e:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

# Beispielaufruf
json_datei = "dino.json"  # Ersetzen Sie dies durch den Pfad zu Ihrer JSON-Datei
check_ids_in_sequence(json_datei)