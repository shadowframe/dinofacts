# dinofacts

## Beschreibung

Die "dinofacts" Anwendung ist eine Streamlit App, die es ermöglicht, Informationen über Dinosaurier anzuzeigen. Die App nutzt eine einfache Benutzeroberfläche, um Daten über verschiedene Dinosaurierarten darzustellen.

Die folgenden Kapitel der Readme beinhalten in der Bezeichnung immer die Python Datei, die für die jeweilige Funktionalität zuständig ist. 

Weitere Informationen befinden sich im [Wiki](https://github.com/shadowframe/dinofacts/wiki) der Anwendung.

### Streamlit Framework
[Streamlit](https://streamlit.io/) ist eine Open-Source-App-Framework. Schau dir das [streamlit cheat-cheat](https://docs.streamlit.io/develop/quick-reference/cheat-sheet) an oder lese die [Installationsanleitung](https://docs.streamlit.io/get-started/installation).

## Daten

Die Daten der Anwendung werden aus einer JSON-Datei geladen, die Informationen über Dinosaurier enthält. Die App bietet Funktionen zum Filtern und Suchen von Dinosauriern nach Namen, Arten und Fortbewegungsarten.

Die Daten selbst stammen von Wikipedia und wurden von mir mithilfe von [restasaurus](https://github.com/vikiru/restasaurus) über die dort zur verfügung getellte [API](https://restasaurus.onrender.com/api/v1) abgerufen. 
Dies führte zu mehreren JSON Dateien, die ich dann in eine einzige Datei zusammengeführt habe und im Nachgang deren Einträge zusätzlich nach deren ID sortiert habe. Diese JSON Dateien in unaufbereiteten Zustand befindet sich im Verzeichnis `data/raw` und die aufbereiteten Daten `dino.json` und `dino_names.json` im Verzeichnis `data`.

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

## 02_fancyText_app.py

Die Datei 02_fancyText_app.py ist eine Streamlit App, die es ermöglicht, Text in einer ansprechenden Weise darzustellen. Die App zeigt einen animierten Text, der nach und nach erscheint.

Als erstes importieren wir die benötigten Bibliotheken:
streamlit damit wir die [streamlit](https://github.com/shadowframe/dinofacts/wiki) Bibliothek nutzen können  und [time](https://docs.python.org/3/library/time.html) für die Zeitverzögerung zwischen den Textteilen.

```
import streamlit as st
import time
```

Als nächstes definieren wir den Text, der animiert angezeigt werden soll. Der Text wird in der Variable `funfact` gespeichert. Hierbei nutzen wir die [Markdown-Syntax](https://docs.streamlit.io/develop/api-reference/text/st.markdown) von Streamlit, um den Text zu formatieren. Emojis und Farben werden verwendet, um den Text ansprechender zu gestalten.
```
funfact = """ 
:rainbow[*Filtere*] :orange[*Namen*] , :green[*Arten*] und :violet[*Fortbewegungsarten*]
"""
````

stream_data() ist eine [Funktion](https://www.w3schools.com/python/python_functions.asp), die den Text in funfact Wort für Wort ausgibt. Jedes Wort wird mit einer Verzögerung von 0.30 Sekunden ausgegeben, um einen animierten Effekt zu erzeugen.
split(" ") teilt den Text in einzelne Wörter auf basierend auf " " also Leerzeichen, und yield gibt jedes Wort zurück, gefolgt von einem Leerzeichen. Die Zeitverzögerung wird mit time.sleep(0.30) erreicht.

Die Funktion wird hier erst definiert, also erstellt. Sie wird noch nicht ausgeführt, sondern nur vorbereitet, damit sie später aufgerufen werden kann.

```
def stream_data():
    for word in funfact.split(" "):
        yield word + " "
        time.sleep(0.30)
```

Das erste Element was tatsächlich in der App angezeigt wird, ist eine Überschrift. Diese wird mit [st.title](https://docs.streamlit.io/develop/api-reference/text/st.title) erstellt.


`st.title("dinoFacts 🦖")`

stream_data() ist eine [Funktion](https://www.w3schools.com/python/python_functions.asp), die aufgerufen werden muss, damit etwas passiert. 
In diesem Fall wird die Funktion verwendet, um den Text zu streamen. Die Funktion wird an [st.write_stream](https://docs.streamlit.io/develop/api-reference/text/st.write_stream) übergeben, die den Text in der App anzeigt.

`st.write_stream(stream_data)`

## loading 03_loadJson_app.py

https://www.w3schools.com/python/python_json.asp



