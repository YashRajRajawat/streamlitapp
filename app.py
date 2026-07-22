import streamlit as st

st.title("My Streamlit App")

st.header("Basic Widgets")

# Text input
user_name = st.text_input("Enter your name:", "Guest")
st.write(f"Hello, {user_name}!")

# Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You are {age} years old.")

# Checkbox
if st.checkbox("Show a secret message"):
    st.success("You found the secret!")