from openai import OpenAI

endpoint = 
deployment_name = 
api_key = 

client=openAI(
    base_rule=endpoint,
    api_key=api_key
)

response = client.response.create(
    model=deployment_name,
    input="What is the capital of France?"
)

print(f"answer: {response.output[0]}")