import argparse
import json
from argparse import RawTextHelpFormatter
import requests
from typing import Optional
import warnings

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "1cfd5561-962a-49e1-a9c7-919e3edb54d1"
FLOW_ID = "3f576e1f-bea3-49b0-a53c-a3c044623cb0"
APPLICATION_TOKEN = "AstraCS:bMDNJTEYYywYDUkFuMJIsbig:e4ceab41db62b9dc82879301803e801c8a9bb9166888d7a8ce7426a1b57da5ca"
ENDPOINT = FLOW_ID + "?stream=false"  # You can set a specific endpoint name in the flow settings

TWEAKS = {
    "ChatInput-NU5on": {},
    "ChatOutput-ZZ8Bh": {},
    "TextInput-LxUPG": {},
    "Prompt-qEjIv": {},
    "ParseData-OQGom": {},
    "AstraDB-qPnEV": {},
    "Google Generative AI Embeddings-fCwrR": {},
    "GoogleGenerativeAIModel-anVZm": {}
}

def run_flow(message: str,
             endpoint: str,
             output_type: str = "chat",
             input_type: str = "chat",
             tweaks: Optional[dict] = None,
             application_token: Optional[str] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def langflow(message, endpoint, tweaks, application_token, output_type, input_type):
    response = run_flow(
        message=message,
        endpoint=endpoint,
        output_type=output_type,
        input_type=input_type,
        tweaks=tweaks,
        application_token=application_token
    )

    # Format response into human-readable format
    try:
        sender_name = response["outputs"][0]["outputs"][0]["results"]["message"]["sender_name"]
        message_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        return f"{sender_name}: {message_text}"
    except KeyError as e:
        warnings.warn(f"KeyError while processing response: {e}")
        return json.dumps(response, indent=2)

def ask_aix(message):
    return langflow(message, ENDPOINT, TWEAKS, APPLICATION_TOKEN, output_type="chat", input_type="chat")
