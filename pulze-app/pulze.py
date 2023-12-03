import json
import openai
import requests

openai.api_key = "sk----2HIAQ6t7PgEdNPvGCaJeAe6e9Asku25qNbAMcMWo_-_W"  # Supply your key however you choose
openai.api_base = "https://api.pulze.ai/v1"  # Enter Pulze's URL

# Make a GET request to the Flask endpoint
response = requests.get("http://localhost:5000/get-response")
if response.status_code == 200:
    question = response.json().get('content')
    print("Input received from the LLM, parsing now!")
    print(f"The results received was {question}")

 # Set up your custom labels and weights
headers = {
    "Pulze-Labels": json.dumps({"foo": "bar", "group": "standard"}),
    "Pulze-Weights": json.dumps({"cost": 0.5, "quality": 0.5, "latency": 0}),
}

text_response = openai.Completion.create(
  model="pulze-v0",
  prompt=f"What would be a good LLM model to answer this type of question: '{question}'?",
  headers=headers,
)

chat_response = openai.ChatCompletion.create(
  model="pulze-v0",
  messages=[{
    "role": "user",
    "content": "Say Hello World!"
  }],
  headers=headers,
)

print(text_response, chat_response)
