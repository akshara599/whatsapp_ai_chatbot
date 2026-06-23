from fastapi import FastAPI, Request
from pydantic import BaseModel
from ai import ask_ai
from whatsapp import send_whatsapp_message

app = FastAPI()


class Message(BaseModel):
    message: str


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/webhook")
def webhook(data: Message):

    try:
        user_text = data.message

        # AI response
        ai_reply = ask_ai(user_text)

        # ❗ IMPORTANT:
        # WhatsApp logic will NOT work in Swagger test
        # because there is no "entry/from" structure here

        return {
            "reply": ai_reply
        }

    except Exception as e:
        print("Error:", e)
        return {"status": "error"}