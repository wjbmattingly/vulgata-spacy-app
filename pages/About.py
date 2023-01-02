import streamlit as st

st.set_page_config(page_title='VulgateAI - About', page_icon = "images/icon.png", layout = 'wide', initial_sidebar_state = 'auto')
with open("README.md", "r") as f:
    data = f.read()
st.markdown(data, unsafe_allow_html=True)
