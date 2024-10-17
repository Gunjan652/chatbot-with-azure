# chatbot-with-azure
# Chatbot Using Azure OpenAI

This project is a web-based chatbot application powered by Azure OpenAI and built using Streamlit. The chatbot is designed to analyze user input, determine its sentiment, and respond with appropriate messages.

## Features
- **Natural Language Processing (NLP):** Uses Azure OpenAI services to analyze user input.
- **Sentiment Analysis:** Determines the sentiment of the user's message to provide more context-aware responses.
- **Interactive Web UI:** Built with Streamlit for a user-friendly chat interface.

## Prerequisites
- Python 3.8 or higher
- Azure account with access to Azure OpenAI services
- Streamlit

## Setup Instructions

### 1. Clone the Repository
Clone the repository to your local machine using:
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
2. Install Dependencies
Make sure you have all the required Python packages by running:

bash
Copy code
pip install -r requirements.txt
3. Azure Setup
Azure OpenAI Account: Make sure you have an Azure account with OpenAI services enabled.
Create a Cognitive Services Resource: Set up your Azure Cognitive Services resource to use the Text Analytics API.
Set Environment Variables: Replace the placeholders in the code with your Azure Text Analytics endpoint and key.
4. Update the Code with Your Azure Credentials
In the app.py file, replace the following with your Azure credentials:

python
Copy code
endpoint = "https://your-resource-name.cognitiveservices.azure.com/"
training_key = "your-azure-key"
5. Run the Chatbot
Start the Streamlit app with the following command:

bash
Copy code
streamlit run app.py
This will launch the chatbot in your default web browser, and you can start interacting with it immediately.

How the Chatbot Works
User Input: The user enters a message into the chatbox.
Sentiment Analysis: The chatbot uses Azure's Text Analytics API to analyze the sentiment of the message.
Response Generation: Based on the sentiment and keywords in the user message, the chatbot generates a response.
Interactive UI: The conversation history is displayed in the chat interface, allowing for a seamless chat experience.
Technologies Used
Azure OpenAI: To perform text analysis and sentiment detection.
Streamlit: For building the interactive web interface.
Python: Programming language used for developing the chatbot logic.
