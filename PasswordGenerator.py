import streamlit as st
import random
import string

st.page(
    page_title = "Password Generator",
    icon = "🔐",
    layout = "centered"
)

st.title("🔐 Password Generator")

len = st.slider("select Password Length" )

uppercase = st.checkbox("Uppercase Letters",value=True)
lowercase = st.checkbox("Lower Letters",value=True)
digit = st.checkbox("Number Letters",value=True)
Symbols = st.checkbox("Symbols Letters",value=True)

def Generate_password(len):

    ch = ""

    if uppercase:
        ch += string.ascii_uppercase
    if lowercase:
        ch += string.ascii_lowercase
    if digit:
        ch += string.digits
    if Symbols:
        ch += string.punctuation
    if not ch:
        return "select at least one option."
    
    password = "".join(random.choice(ch)) for _ in range(len)
    return password


    
    