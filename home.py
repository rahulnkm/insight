import streamlit as st
import time

input = st.text_area("Write something")

messages = []

if input:
    messages.append(input)


display = st.button("Show messages")

if display:
    temp_message = st.empty()
    temp_message.write(messages)
    time.sleep(4)
    temp_message.empty()