from fastapi import FastAPI, Request
import os

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


# -------------------------
# 1. WEBHOOK VERIFY (GET)
# -------------------------
@app.get("/webhook")
def verify_webhook(request: Request):
    params = request.query_params
afrom fastapi import FastAPI, Request

app = FastAPI()


VERIFY_TOKEN = "mysecret123"


# 🔵 STEP 1: Meta verification (IMPORTANT)
@app.get("/webhook")
def verify_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)

    return {"error": "verification failed"}


# 🔵 STEP 2: Incoming messages
@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    print(data)

    return {"status": "ok"}
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)

    return "Verification failed"


# -------------------------
# 2. RECEIVE MESSAGE (POST)
# -------------------------
@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]

        user_text = message["text"]["body"]
        user_number = message["from"]

        # AI response
        ai_reply = ask_ai(user_text)

        # send reply to WhatsApp
        send_whatsapp_message(user_number, ai_reply)

        return {"status": "sent"}

    except Exception as e:
        print("Error:", e)
        return {"status": "error"}