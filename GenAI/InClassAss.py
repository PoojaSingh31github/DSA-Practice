from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key="sk-proj-W3uDUc55mnT3BlbkFJ5NPSaf8RdinOC6p9HtRQ"
)

st.title("Multi-Functional Generator")

# Dropdown to select type of generation
generation_type = st.selectbox("Select the type of generation", ["food", "Shayari"])

# Input field for user details
user_input = st.text_input(f"Enter the details for {generation_type.lower()}:")

if st.button("Generate"):
    if user_input:
        try:
            if generation_type == "Email":
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You have good best knowledge in food of diffrent countries. and you know all the famous food items according to diffrennt locations"},
                        {"role": "user", "content": f"best food of diffrent countries and location : {user_input}"}
                    ]
                )
                result = completion.choices[0].message['content']
                st.text_area("Generated output", result, height=300)
            
            elif generation_type == "Shayari":
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a Shayari expert in traslating the Shayari in any languege by getting it from any language"},
                        {"role": "user", "content": f"translate a Shayari based on the keyword: {user_input}"}
                    ]
                )
                result = completion.choices[0].message['content']
                st.text_area("Generated Shayari", result, height=300)
        
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error(f"Please enter the details for {generation_type.lower()}.")