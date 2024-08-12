from openai import OpenAI
import streamlit as st

client = OpenAI(
    api_key=""
)

st.title("Multi-Functional Generator")

# Dropdown to select type of generation
generation_type = st.selectbox("Select the type of generation", ["Text Generation", "Text Summarization", "Language Translation"])

# Input field for user details
user_input = st.text_input(f"Enter the details for {generation_type.lower()}:")

if st.button("Generate"):
    if user_input:
        try:
            if generation_type == "Text Generation":
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert in generating detailed and engaging text about various topics."},
                        {"role": "user", "content": f"Describe the on the given topic : {user_input}"}
                    ]
                )
                result = completion.choices[0].message['content']
                st.text_area("Generated output", result, height=300)
            
            elif generation_type == "Text Summarization":
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert in summarizing text concisely and clearly."},
                        {"role": "user", "content": f"Summarize the following text: {user_input}"}
                    ]
                )
                result = completion.choices[0].message['content']
                st.text_area("Summarized Text", result, height=300)

            elif generation_type == "Language Translation":
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an expert in translating text accurately and fluently between different languages."},
                        {"role": "user", "content": f"Translate the following text into the desired language: {user_input}"}
                    ]
                )
                result = completion.choices[0].message['content']
                st.text_area("Translated Text", result, height=300)
        
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error(f"Please enter the details for {generation_type.lower()}.")
