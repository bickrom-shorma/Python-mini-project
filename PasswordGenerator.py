import streamlit as st
import random
import string



st.title("🔐 Password Generator")

length = st.slider("Select Password Length", 4, 50, 12)

use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_digits = st.checkbox("Include Numbers", value=True)
use_symbols = st.checkbox("Include Symbols", value=True)


def generate_password(length):
    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one option."

    password = "".join(random.choice(characters) for _ in range(length))
    return password


