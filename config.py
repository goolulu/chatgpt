import os

import httpx
from openai import OpenAI

OPENAI_API_KEY = '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'

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

client = httpx.Client(proxy='http://127.0.0.1:1080')
client = OpenAI(http_client=client)
