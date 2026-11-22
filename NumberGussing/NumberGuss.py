import streamlit as st
import random

st.title(":blue[Number Guessing Game]")
st.divider()

if "random_number" not in st.session_state:
    st.session_state.random_number = random.randint(1, 100)
    st.session_state.att = 0  
random_number = st.session_state.random_number

col1, col2 = st.columns([3, 1])

with col1:
    user_guess = st.number_input("Enter your chosen number", value=None)

with col2:
    st.metric("Attempts", f"{st.session_state.att}/5")


if st.button("New Game"):
  st.session_state.random_number = random.randint(1, 100)
  st.session_state.att = 0
  st.rerun()
    

if st.session_state.att >= 5:
    st.error(f" Game Over! The correct number was: {random_number}")
    if st.button("Play Again"):
        st.session_state.random_number = random.randint(1, 100)
        st.session_state.att = 0
        st.rerun()
else:
    if user_guess is not None:
        guess = int(user_guess)
        
        if guess == random_number:
            st.success("✅ Well Played!")
            st.session_state.att += 1
            if st.button("Play Again"):
                st.session_state.random_number = random.randint(1, 100)
                st.session_state.att = 0
                st.rerun()
        elif guess < random_number:
            st.warning(f"⬆️ Lower - Remaining: {5 - st.session_state.att - 1}")
            st.session_state.att += 1
        else:
            st.warning(f"⬇️ Higher - Remaining: {5 - st.session_state.att - 1}")
            st.session_state.att += 1
    else:
        st.info("Please enter a number")