from dotenv import load_dotenv 
from google import genai 
import os 
import pandas as pd

## Load environment variables from .env file
load_dotenv()

## Variables
cwd = os.getcwd() 
input = os.path.join(cwd, "input") 
output = os.path.join(cwd, "output")

client = genai.Client(api_key=os.environ['GOOGLE_API_KEY'])

response = client.models.generate_content(
    model="gemma-3-27b-it", 
    contents="Tell me about yourself",
)

print(response.text)



