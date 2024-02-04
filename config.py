import os

import httpx
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from openai import OpenAI

load_dotenv('api.env')
os.environ['OPENAI_API_KEY'] = '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'
os.environ['OPENAI_BASE_URL'] = f"https://api.openai-proxy.com/v1"

#
llm = ChatOpenAI(model_name='gpt-3.5-turbo-1106')
client = OpenAI()

embeddings_model = OpenAIEmbeddings(),
