import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def setup_gemini():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_summary(metrics):
    setup_gemini()

    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    prompt = f"""
    You are a senior site reliability engineer.

    Analyze the following web traffic metrics:

    {metrics}

    Give:
    - Key trends
    - Any anomalies
    - Possible causes
    - Recommendations
    """

    response = model.generate_content(prompt)
    return response.text


def ask_question(metrics, question):
    setup_gemini()

    model = genai.GenerativeModel("gemini-2.5-flash-lite")

    prompt = f"""
    You are a senior site reliability engineer.

    Here are web traffic metrics:
    {metrics}

    Question: {question}
    """

    response = model.generate_content(prompt)
    return response.text