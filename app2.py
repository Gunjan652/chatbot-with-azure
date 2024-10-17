import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
azure_oai_key = os.getenv("AZURE_OAI_KEY")
azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

# Streamlit app
st.title("Azure OpenAI chatbot App")
st.write("Enter a prompt to get a response from the Azure OpenAI model.")

# Input text box for user prompt
input_text = st.text_area("Enter your prompt here:", "")

if st.button("Submit") and input_text:
    st.write("Sending request to Azure OpenAI...")

    # Prepare the request payload
    headers = {
        "Content-Type": "application/json",
        "api-key": azure_oai_key
    }
    data = {
        "prompt": input_text,
        "max_tokens": 100
    }

    # Send the request to Azure OpenAI
    response = requests.post(
        f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}/completions?api-version=2022-12-01",
        headers=headers,
        json=data
    )

    # Check the response
    if response.status_code == 200:
        result = response.json()
        st.write("Response from Azure OpenAI:")
        st.success(result['choices'][0]['text'].strip())
    else:
        st.error(f"Error {response.status_code}: {response.text}")
