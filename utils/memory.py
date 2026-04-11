import streamlit as st

def init_memory():
    if "history" not in st.session_state:
        st.session_state.history = []

def add_to_memory(user, response):
    st.session_state.history.append({
        "user": user,
        "response": response
    })

def get_memory():
    return st.session_state.history