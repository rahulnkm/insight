import streamlit as st

input = st.text_area("Write something")

messages = []

if input:
    messages.append(input)


display = st.button("Show messages")

if display:
    st.write(messages)