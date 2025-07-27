# Dino-Facts Daten

dino.json enthält nun die Daten für die Dino-Facts
check.py prüft, ob die IDs in der dino.json aufsteigend und lückenlos sind.

## Daten       
Die Daten für die Dino-Facts sind in der Datei `dino.json` gespeichert. Diese Datei enthält Informationen über verschiedene Dinosaurierarten, einschließlich ihrer Namen, Beschreibungen und anderer interessanter Fakten.

## Datenintegrität
Um die Integrität der Daten zu gewährleisten, wurde ein Test geschrieben, der sicherstellt, dass die Daten in der `dino.json` Datei umfänglich vorhanden sind. Dies wird durch die Datei `check.py` überprüft. Der Test prüft, ob alle IDs in der JSON-Datei aufsteigend und lückenlos sind.

Um die Datenintegrität zu testen, kannst du den folgenden Befehl in deinem Terminal ausführen:
`python check.py` bzw `python3 check.py`