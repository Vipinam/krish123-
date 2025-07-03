import streamlit as st
st.title("intractive streamlit app")
name=st.text_input("enter your name:")
if st.button("submit"):
    st.write(f"hello,{name}!welcome to streamlit,")
