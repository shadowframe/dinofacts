# dinofacts

## Beschreibung

Die "dinofacts" Anwendung ist eine Streamlit App, die es ermöglicht, Informationen über Dinosaurier anzuzeigen. Die App nutzt eine einfache Benutzeroberfläche, um Daten über verschiedene Dinosaurierarten darzustellen.

Die folgenden Kapitel der Readme beinhalten in der Bezeichnung immer die Python Datei, die für die jeweilige Funktionalität zuständig ist. 

Weitere Informationen befinden sich im [Wiki](https://github.com/shadowframe/dinofacts/wiki) der Anwendung.

## Installation 01_start_app.py

### Clone das Repo auf deinen Rechner oder Server:

`git clone git@github.com:shadowframe/dinofacts.git`

Wechsle in das Verzeichnis:

`cd dinofacts`

### Erstelle eine Virtuelle Python Umgebung und aktiviere sie

**Wenn du Windows nutzt beachte unbedingt,** dass die Befehle anders lauten als auf MacOS und Linux, du findetst die Windows Befehle auf folgender Seite:

https://www.w3schools.com/python/python_virtualenv.asp

`python -m venv .venv` 

`source .venv/bin/activate`

### Streamlit installieren

#### Option 1 requirements.txt

Mithilfe der requirements.txt kann man per PythonPaketVerwaltung "pip" einfach viele Python Bibliotheken installieren ohne diese Einzeln eingeben zu müssen. Die requirements.txt beinhaltet den Namen jeden Pakets untereinander geschrieben.

`pip install -r requirements.txt`

#### Option 2 pip

`pip install streamlit`

## Starten der Anwendung

`streamlit run 01_start_app.py`

### Port definieren

Standardmäßig läuft die Anwendung auf Port 8501. Wenn du einen anderen Port nutzen möchtest, kannst du dies mit dem folgenden Befehl tun: 

`streamlit run 01_start_app.py --server.port=80`

## Installation 02_fancyText_app.py



