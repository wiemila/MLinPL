import pandas as pd
import streamlit as st

st.title("Widgets Playground")

st.header("Part 1: Experimenting", divider="violet")

############################################################################
# Set the options and the questions

seasons = ["Spring", "Summer", "Autumn", "Winter"]
question = "What's your favourite season?"

############################################################################

st.subheader("Radio", divider="gray")
st.caption("You can only pick one")

season_selected = st.radio(label=question, options=seasons)
st.write(f"Your favourite season is {season_selected}")

############################################################################

st.subheader("Dropdown / selectbox", divider="gray")
st.caption("You can only pick one")

season_selected_drop_down = st.selectbox(question, options=seasons)
st.write(f"Your favourite season is {season_selected_drop_down}")

############################################################################

st.subheader("Multiselect", divider="gray")
st.caption("You can pick many")

season_selected_multi = st.multiselect(question, options=seasons)
st.write(f"Your favourite seasons are: {season_selected_multi}")

############################################################################

st.subheader("Checkbox", divider="gray")

# Create a dictionary of the labels and the current state
options = {option: None for option in seasons}

# Loop through the dictionary to create the checkbox and write the current value
for option, checkbox in options.items():
    options[option] = st.checkbox(option)

for option, checkbox in options.items():
    if checkbox:
        st.write(f"You like {option}")

############################################################################

st.subheader("Toggle", divider="gray")

# Create a dictionary of the labels and the current state
options = {option: None for option in seasons}

# Loop through the dictionary to create the checkbox and write the current value
for option, checkbox in options.items():
    options[option] = st.toggle(option)

for option, checkbox in options.items():
    if checkbox:
        st.write(f"You like {option}")

#duplicate widget id if two widgets have the same name
