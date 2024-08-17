import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
import os
from dotenv import load_dotenv

# 環境変数をenvファイルから読み込む
load_dotenv()

# 環境変数からAPIキーを取得
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
# print(f"GOOGLE_API_KEY: {GOOGLE_API_KEY}")

import requests

headers = {
    'Content-Type': 'application/json',
}

params = {
    'key': 'AIzaSyBqQ3digDCAjmIQ0VzkVX1gwViAHGuA3jw',
}

json_data = {
    'contents': [
        {
            'parts': [
                {
                    'text': 'Explain how AI works',
                },
            ],
        },
    ],
}

response = requests.post(
    'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent',
    params=params,
    headers=headers,
    json=json_data,
)

print(response)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"contents":[{"parts":[{"text":"Explain how AI works"}]}]}'
#response = requests.post(
#    'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent',
#    params=params,
#    headers=headers,
#    data=data,
#)