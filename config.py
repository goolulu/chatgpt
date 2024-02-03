import os

import httpx
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI

load_dotenv('api.env')
os.environ['OPENAI_API_KEY'] = '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'
http_client = httpx.Client(proxy='http://127.0.0.1:1080')


llm = ChatOpenAI(api_key='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',
                 model_name='gpt-3.5-turbo-1106',
                 http_client=http_client)
client = OpenAI(http_client=http_client)
