import streamlit as st
import time

funfact = """ 
:rainbow[*Filtere*] :orange[*Namen*] | :green[*Arten*] | :violet[*Fortbewegungsarten*]
"""

def stream_data():
    for word in funfact.split(" "):
        yield word + " "
        time.sleep(0.30)

st.title("dinoFacts 🦖")
st.write_stream(stream_data)
 