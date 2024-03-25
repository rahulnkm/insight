import streamlit as st

input = st.text_area("Write something")

messages = []

if input:
    messages.append(input)


display = st.button("Show messages")

if display:
    
    temp_message = st.empty()
    
    # Display the array contents in the placeholder
    temp_message.write(messages)
    
    # Sleep for 4 seconds, showing the contents
    time.sleep(4)
    
    # Clear the placeholder after 4 seconds, effectively hiding the array contents
    temp_message.empty()