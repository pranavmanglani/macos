import streamlit as st

# Inject custom CSS
st.markdown("""
    <style>
        .css-1d391kg { background-color: #f0f0f5; }
        .css-1d391kg > div:first-child { background-color: #2c3e50; color: white; }
    </style>
""", unsafe_allow_html=True)

# Top navigation bar
st.markdown("<h1 style='text-align: center; color: white;'>My macOS Desktop</h1>", unsafe_allow_html=True)

# Sidebar as dock
with st.sidebar:
    st.button("App 1")
    st.button("App 2")
    st.button("App 3")

# Main content area
st.write("Welcome to your macOS-like desktop environment!")
