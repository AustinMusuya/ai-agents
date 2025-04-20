from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
# from azure.ai.inference.models import SystemMessage, UserMessage
import openai
import os
from dotenv import load_dotenv
load_dotenv()

try:
    # Initialize the project client
    project_connection_string = os.getenv("PROJECT_CONNECTION_STRING")
    project_client = AIProjectClient.from_connection_string(
        credential=DefaultAzureCredential(), conn_str=project_connection_string)

    # Get an Azure OpenAI chat client
    opneai_client = project_client.inference.get_azure_openai_client(
        api_version="2024-12-01-preview")

    # Get a chat client
    # chat = project_client.inference.get_chat_completions_client()

    # Get a chat completion based on a user-provided prompt
    user_prompt = input("Enter a question: ")

    response = opneai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
                "content": "You are a helpful AI assistant that answers questions."},
            {"role": "user", "content": user_prompt}
        ],
    )

    print(response.choices[0].message.content)

except Exception as ex:
    print(ex)
