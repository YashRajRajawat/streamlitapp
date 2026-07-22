import streamlit as st

st.title("Interactive Streamlit Demo")

st.write("Let's explore some interactive widgets!")

# Selectbox
option = st.selectbox(
    "Which is your favorite fruit?",
    ('Apple', 'Banana', 'Cherry', 'Date'))
st.write(f"You selected: {option}")

# Button
if st.button("Click me!"):
    st.balloons()
    st.success("You clicked the button!")

# Text area
user_text = st.text_area("Tell me something interesting:", "Type here...")
st.write(f"You wrote: {user_text}")