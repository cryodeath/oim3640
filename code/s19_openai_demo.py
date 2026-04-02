from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

response = client.responses.create(
    model='gpt-5-nano', input=" Write me a haiku about the cherry blossoms in Boston in the spring."
)

print(response.output_text)
