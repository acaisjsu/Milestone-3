import streamlit as st
import openai 
from openai import OpenAI
import pandas as pd
import os

openai.api_key = os.environ
client = OpenAI()
 
uploaded_file = st.file_uploader("Upload your water quality dataset (CSV)", type=["csv"])
st.title("Water Quality Q&A Bot")
if st.button("Important Key Terms"):
    st.write("pH")
    st.write("Turbidity")
    st.write("Nitrate")
    st.write("Phosphate")
    st.write("Dissolved Oxygen")
prompt = st.text_input("Enter any questions about water quality or upload data about water quality and I will answer your questions with detailed explanations.")
if uploaded_file:
    df = pd.read_csv(uploaded_file) 
def get_completion(prompt, model="gpt-3.5-turbo"):
    completion = client.chat.completions.create(
        model=model,
        messages=[
        {"role": "system", "content": "You are a professional water quality expert and you will provide detailed explanations to the given prompts or questions about the given datasets."}, 
        {"role": "user", "content": prompt},
        ]
    )
    return completion.choices[0].message.content

with st.form(key = "chat"):    
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(get_completion(prompt)) 
        
        


 
        





