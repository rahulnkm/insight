import streamlit as st

input = st.text_area("Write something")

messages = []

if input:
    messages.append(input)


display = st.button("Show messages")

array_placeholder = st.empty()

if display:
    
    array_placeholder.write(my_array)
    
    # Wait for 4 seconds
    time.sleep(4)
    
    # Clear the content after 4 seconds
    array_placeholder.empty()