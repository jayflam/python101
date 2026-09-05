from openai import OpenAI
import os

endpoint = "https://az-103-study-jl1.services.ai.azure.com/openai/v1/chat/completions"
deployment_name = "grok-4.3"
api_key = os.getenv("API_KEY")
client=openAI(
    base_rule=endpoint,
    api_key=api_key
)

response = client.response.create(
    model=deployment_name,
    input="What is the capital of France?"
)

print(f"answer: {response.output[0]}")