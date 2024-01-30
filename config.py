import os

import httpx
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv('api.env')

client = httpx.Client(proxy='http://127.0.0.1:1080')
client = OpenAI(http_client=client)
