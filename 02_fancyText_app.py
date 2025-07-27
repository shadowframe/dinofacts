import streamlit as st
import time

st.title("dinoFacts 🦖")
st.markdown("""
Willkommen zu meiner App! 
- **Dinos 🦖** nach :orange[*Namen*] suchen
- **Dinos 🦖** nach :green[*Arten*] filtern
""") 

def stream_data():
    for word in funfact.split(" "):
        yield word + " "
        time.sleep(0.10)


funfact = """
Du wusstest bestimmt schon, dass Dinos 🦖 vor Millionen von Jahren lebten.
            
Aber wusstest  du auch, dass du Dinos 🦖 in dieser App nach ihren Essgewohnheiten filtern kannst? Egal ob Allesfresser, Pflanzenfresser oder Fleischfresser, hier findest du die passenden Dinos 🦖!
"""

st.write_stream(stream_data)