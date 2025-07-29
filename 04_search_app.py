import streamlit as st
import time
import json

funfact = """
:rainbow[*Filtere*] :orange[*Namen*] | :green[*Arten*] | :violet[*Fortbewegungsarten*]
"""

### Functions ###

def stream_data():
    for word in funfact.split(" "):
        yield word + " "
        time.sleep(0.30)

# Load the dino.json file
def load_dino_data():
    with open("data/dino_names.json", "r") as file:  # Adjust the path if necessary
        return json.load(file)

@st.fragment
def fancy_text():
    st.write_stream(stream_data)

@st.fragment
def search():
    # Autocomplete search
    st.markdown("### **Search for a Dinosaur:**")

    # Create a list of dinosaur names for selection
    dino_names = [dino['name'] for dino in dino_data]

    # Add a selectbox for dinosaur selection
    selected_dino_name = st.selectbox("Select a Dinosaur:", dino_names)

    # Find the corresponding ID for the selected dinosaur
    selected_dino_id = next((dino['id'] for dino in dino_data if dino['name'] == selected_dino_name), None)

    # Display the selected dinosaur's name and ID
    if selected_dino_name:
        st.write(f"Selected Dinosaur Name: {selected_dino_name}")
        st.write(f"Selected Dinosaur ID: {selected_dino_id}")

# Load the data of the dinosaurs names and id´s
dino_data = load_dino_data()

### GUI ###
st.title("dinoFacts 🦖")

fancy_text()

search()
