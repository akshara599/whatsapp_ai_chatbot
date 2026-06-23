import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_ai(message, retries=3):
    for i in range(retries):
        try:
            response = model.generate_content(message)
            return response.text

        except Exception as e:
            print("AI error:", e)

            # If rate limit → wait before retry
            time.sleep(2 ** i)

    return "Sorry, AI is busy right now. Try again later."