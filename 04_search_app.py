import streamlit as st
import time
import json

funfact = """
:rainbow[*Filtere*] :orange[*Namen*] | :green[*Arten*] | :violet[*Fortbewegungsarten*]
"""

def stream_data():
    for word in funfact.split(" "):
        yield word + " "
        time.sleep(0.30)

# Load the dino.json file
def load_dino_data():
    with open("data/dino_names.json", "r") as file:  # Adjust the path if necessary
        return json.load(file)

st.title("dinoFacts lala 🦖")
st.write("Ich bin der Commit vom Macbook Air2")
st.write_stream(stream_data)

# Display the loaded JSON data
dino_data = load_dino_data()
st.json(dino_data)  # Use Streamlit's st.json to display JSON data nicely
