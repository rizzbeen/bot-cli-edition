import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API NOT FOUND")
genai.configure(api_key=api_key)

def gemini(prompt):
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    result = model.generate_content(prompt)
    return result.text