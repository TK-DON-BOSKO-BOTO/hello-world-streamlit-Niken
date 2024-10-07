import streamlit as st

st.title("🎈 hello word")

name = st.text_input("nama")

if (name):
    st.write("hallo, nama saya : ", name)
else:
    st.warning("please, input your name!!!")

