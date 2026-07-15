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