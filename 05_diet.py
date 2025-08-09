import streamlit as st
import time
import json

funfact = """
:rainbow[*Filtere*] :orange[*Namen*] | :green[*Arten*] | :violet[*Fortbewegungsarten*]
"""

### Functions ###
print("Variable funfact wird an dieser Stelle ausgegeben")
def stream_data():
    for word in funfact.split(" "):
        yield word + " "
        time.sleep(0.30)

# Load the dino_names.json file and parse it into a Python dictionary
def load_dino_data():
    with open("data/dino_names.json", "r") as file:  # Adjust the path if necessary
        return json.load(file)

def load_all_dino_data():
    with open("data/dino.json", "r") as file:  # Adjust the path if necessary
        return json.load(file)
    
def get_diet_by_id(dino_data, dino_id):
    # Search for the dinosaur with the matching ID
    for dino in dino_data:
        if dino.get("id") == dino_id:
            return dino.get("diet", "Diet information not available")
    return "Dinosaur with the given ID not found"

def get_diet_image_by_diet(diet):
    if diet == "herbivore":
        st.image("images/herbivore.png", caption="Herbivore diet image", use_container_width=True)
    if diet == "carnivore":
        st.image("images/carnivore.png", caption="Carnivore diet image", use_container_width=True)
    if diet == "omnivore":
        st.image("images/omnivore.png", caption="Omnivore diet image", use_container_width=True)




### Functions ###
# fancy_text returns a stream of text from the stream_data function
@st.fragment
def fancy_text():
    st.write_stream(stream_data)

# search creates a search bar and displays the selected dinosaur's name and ID
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

    # Display the selected dinosaur's name and ID and diet and so on
    if selected_dino_name:
        st.write(f"Selected Dinosaur Name: {selected_dino_name}")
        st.write(f"Selected Dinosaur ID: {selected_dino_id}")
        # Load the data
        all_dino_data = load_all_dino_data()
        dino_id = selected_dino_id
        diet = get_diet_by_id(all_dino_data, dino_id)
        st.write(f"The diet for dinosaur with ID {dino_id} is: {diet}")
        get_diet_image_by_diet(diet)

# Load the data of the dinosaurs names and id´s
dino_data = load_dino_data()

### GUI ###
st.title("dinoFacts 🦖")

fancy_text()

search()
