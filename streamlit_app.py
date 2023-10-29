import streamlit as st
st.title("welcome ML in PL 23")
st.header("Good luck in the tutorial")
st.subheader("at Politechnika Maths")

#Play with markdown
st.markdown("""
Lorem**ipsum**

-:balloon: Chemistry

-:car: Data Science

$a+a^2$

Have a good coffee

I am a deep learning expert 
""", unsafe_allow_html=True)

#Create a button
#every time you interact the whole script reruns from top to bottom
#st.help(st.button)
#clicked = st.button(label="Click me")
#st.write(clicked)
clicked = st.button(label="send baloons")
if clicked:
  st.ballons()


