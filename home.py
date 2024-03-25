import streamlit as st
import time

if 'text_area_content' not in st.session_state:
    st.session_state.text_area_content = ''

with st.form("my_form"):
    user_input = st.text_area("Enter text here:", key='text_area_content')
    submitted = st.form_submit_button("Submit")

if submitted:
    st.session_state.text_area_content = ''

messages = []

if input:
    messages.append(input)
    st.session_state.text_area_content = ''

display = st.button("Show messages")

if display:
    temp_message = st.empty()
    temp_message.write(messages)
    time.sleep(4)
    temp_message.empty()