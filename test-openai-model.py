# import os
# from dotenv import load_dotenv

# # Add Azure OpenAI package
# from azure.ai.openai import OpenAIClient
# from azure.core.credentials import AzureKeyCredential


# def main(): 
        
#     try: 
    
#         # Get configuration settings 
#         load_dotenv()
#         azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
#         azure_oai_key = os.getenv("AZURE_OAI_KEY")
#         azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        
#         # Initialize the Azure OpenAI client...
#         credential = DefaultAzureCredential()
#         client = OpenAIClient(azure_oai_endpoint, credential)


#         while True:
#             # Get input text
#             input_text = input("Enter the prompt (or type 'quit' to exit): ")
#             if input_text.lower() == "quit":
#                 break
#             if len(input_text) == 0:
#                 print("Please enter a prompt.")
#                 continue

#             print("\nSending request for summary to Azure OpenAI endpoint...\n\n")
            
#             # Add code to send request...
#             response = client.get_completions(
#                 deployment_id=azure_oai_deployment,
#                 prompt=input_text,
#                 max_tokens=100
#             )

            
            
            

#     except Exception as ex:
#         print(ex)

# if __name__ == '__main__': 
#     main()
import os
import requests
from dotenv import load_dotenv

def main():
    try:
        # Load configuration settings from the .env file
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")

        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            print("\nSending request to Azure OpenAI endpoint...\n")

            # Prepare the request payload
            headers = {
                "Content-Type": "application/json",
                "api-key": azure_oai_key
            }
            data = {
                "prompt": input_text,
                "max_tokens": 100
            }

            # Send request to Azure OpenAI
            response = requests.post(
                f"{azure_oai_endpoint}/openai/deployments/{azure_oai_deployment}/completions?api-version=2022-12-01",
                headers=headers,
                json=data
            )

            # Check if the request was successful
            if response.status_code == 200:
                result = response.json()
                print(f"Response: {result['choices'][0]['text'].strip()}\n")
            else:
                print(f"Error: {response.status_code} - {response.text}")

    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == '__main__': 
    main()
