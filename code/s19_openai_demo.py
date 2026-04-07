from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model='gpt-5-nano', input=" help me research what is the difference between an ai model and ai agent."
)

print(response.output_text)
