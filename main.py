from google import genai 
from google.genai import types 
from PIL import Image 
from io import BytesIO
import pandas as pd
from init import init
import base64 

import os 

## Load environment variables from .env file
init()

## Variables
cwd = os.getcwd() 
input = os.path.join(cwd, "input", "resume-dataset") 
output = os.path.join(cwd, "output")

user_profile = { 
    "education": "B.Tech in Computer Science",
    "experience": "2 years as a frontend developer (React)",
    "skills": ["JavaScript", "HTML", "CSS"], 
    "goal": "Switch to Data Analyst role", 
}

expected_output = { 
    "recommeded_roles":["Data Analyst", "Business Intelligence Developer"], 
    "skill_gaps": ["SQL", "Data Visualization", "Python"],
    "courses_suggested": [
        {"name": "Data Analytics with Python", "platform": "Coursera"}, 
        {"name": "SQL for Data Science", "platform": "Udemy"}
    ]
}

examples = [
    {

    }
]

csv_file = os.path.join(input, "Resume", "Resume.csv")
print(csv_file)

df = pd.read_csv(csv_file)
print(df.head())
client = genai.Client(api_key=os.environ['GOOGLE_API_KEY'])
contents = (
    "creat a 3d image of hyper realistic baby cat playing, "
    "in the levish farm house with her friends."
    )

response = client.models.generate_content(
    # model="gemma-3-27b-it", 
    model = "gemini-2.0-flash-exp", 
    contents= contents, 
    config=types.GenerateContentConfig(
        response_modalities=['Text', 'Image']
    )
)

print("Response: ", response)

for part in response.candidates[0].content.parts:
    if part.text is not None: 
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO((part.inline_data.data)))
        image.save(os.path.join(output, "images", 'gemini-native-image.png'))
        image.show() 