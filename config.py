import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "your_groq_api_key_here"
MODEL_NAME = "llama-3.3-70b-versatile"
