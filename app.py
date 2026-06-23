from fastapi import FastAPI, Request
from ai import ask_ai
from whatsapp import send_whatsapp_message

app = FastAPI()


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]

        user_text = message["text"]["body"]
        user_number = message["from"]

        # AI response
        ai_reply = ask_ai(user_text)

        # send back to WhatsApp
        send_whatsapp_message(user_number, ai_reply)

        return {"status": "sent"}

    except Exception as e:
        print("Error:", e)
        return {"status": "error"}