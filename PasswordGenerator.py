import streamlit as st
import random
import string

# Page Configuration
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Password Generator")

# Password Length
length = st.slider("Select Password Length", 4, 50, 12)

# Options
use_uppercase = st.checkbox("Include Uppercase Letters")
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_numbers = st.checkbox("Include Numbers", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)

# Generate Button
if st.button("Generate Password"):

    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if characters == "":
        st.error("Please select at least one character type.")

    else:
        password = ""

        for i in range(length):
            password += random.choice(characters)

        st.success("Password Generated Successfully!")
        st.code(password)