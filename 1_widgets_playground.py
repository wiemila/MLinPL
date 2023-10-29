## different pages will be different apps in streamlit i dont know how to do it in github

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
#for option, checkbox in options.items():
#    options[option] = st.toggle(option)
#
#for option, checkbox in options.items():
#    if checkbox:
#        st.write(f"You like {option}")

#duplicate widget id if two widgets have the same name
activated_multiproc =st.toggle(
    "do you want to activate multiprocessing?"
)
activated_multiproc

############################################################################

st.subheader("Slider", divider="gray")

slider_value = st.slider(
    f"As a %, How much do you love {season_selected}",
    min_value=0,
    max_value=100,
    value=(20,30),
    #if put like this in the () its a range slider, if just one value its the default value
    step=5,
    format="%d%%",
    help="Pick something between 0 and 100",
)

st.write(f"You like {season_selected} {slider_value}%")

############################################################################

st.subheader("Select Slider", divider="gray")
st.write(
    st.select_slider(
        "Question", ["Very low", "low", "medium", "high"]
    )
)

#slider_item = st.select_slider(
#    label=f"How much do you like {season_selected_drop_down}",
#    options=["I don't", "A little", "A lot", "It's the Best!"],
#)

#st.write(f"You like {season_selected_drop_down} {slider_item.lower()}!")

############################################################################

st.subheader("Text Input", divider="gray")

season = st.text_input(
    "What's your favorite season :balloon:?"
)
st.write(season)

############################################################################

st.subheader("Number Input", divider="gray")

user_number (
   :number of components to keepi n PCA:",
min_value=1,
step=1,
)

#########################################
