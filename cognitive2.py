from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import streamlit as st

# Replace with your Azure Text Analytics endpoint and training key
endpoint = "https://kshitiik.cognitiveservices.azure.com/"
training_key = "a472dc14799640bca6811ca07f52ea41"

# Function to authenticate client
def authenticate_client():
    ta_credential = AzureKeyCredential(training_key)
    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=ta_credential)
    return text_analytics_client

# Function to generate a response to the user's question
def generate_response(client, user_input):
    try:
        # Analyze the sentiment of the user input
        response = client.analyze_sentiment(documents=[user_input])[0]
        sentiment = response.sentiment
        
        # Basic rule-based response based on sentiment
        if "weather" in user_input.lower():
            reply = "I'm not sure about the weather right now, but you can check your favorite weather app."
        elif "name" in user_input.lower():
            reply = "I am a chatbot powered by Azure AI services. Nice to meet you!"
        elif sentiment== "what is ai":
            reply = "Artificial intelligence (AI) is a set of technologies that enable computers to perform a variety of advanced functions, including the ability to see, understand and translate spoken and written language, analyze data, make recommendations, and more."
        elif sentiment == "ml":
            reply = "Machine learning (ML) is a field of study in artificial intelligence concerned with the development and study of statistical algorithms that can learn from data and generalize to unseen data, and thus perform tasks without explicit instructions."
        elif sentiment =="azure":
            reply="The Azure cloud platform is more than 200 products and cloud services designed to help you bring new solutions to life—to solve today’s challenges and create the future. Build, run, and manage applications across multiple clouds, on-premises, and at the edge, with the tools and frameworks of your choice."
        else:
            reply = "That's interesting! What else would you like to know?"
            
        return reply
    except Exception as err:
        return f"Error occurred: {err}"

# Initialize the chatbot
client = authenticate_client()
print("Hello! I am your Azure-based chatbot. Type 'quit' to exit.")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    response = generate_response(client, user_input)
    print(f"Chatbot: {response}")
    st.title("Azure AI Chatbot")

# Initialize the Azure Text Analytics client when the app starts
if 'client' not in st.session_state:
    st.session_state.client = authenticate_client()

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for chat in st.session_state.chat_history:
    st.write(f"**You:** {chat['user_input']}")
    st.write(f"**Chatbot:** {chat['response']}")

# User input
user_input = st.text_input("Ask me anything:", key="user_input")

# Generate response when the user inputs a message
if user_input:
    response = generate_response(st.session_state.client, user_input)
    st.session_state.chat_history.append({"user_input": user_input, "response": response})
    st.experimental_rerun()
