from google import genai 
import pandas as pd
from init import init

import os 

## Load environment variables from .env file
init()

## Variables
cwd = os.getcwd() 
input = os.path.join(cwd, "input") 
output = os.path.join(cwd, "output")

print("input", input)
print("output", output)

client = genai.Client(api_key=os.environ['GOOGLE_API_KEY'])

response = client.models.generate_content(
    model="gemma-3-27b-it", 
    contents="I want to interface audio input to user, how can i use audio input in my code? and provide you",
)

print(response.text)



