from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

VERIFY_TOKEN = "mysecret123"


# -------------------------
# 1. WEBHOOK VERIFICATION (GET)
# -------------------------
@app.get("/webhook")
def verify_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)

    return PlainTextResponse("Verification failed", status_code=403)


# -------------------------
# 2. RECEIVE MESSAGES (POST)
# -------------------------
@app.post("/webhook")
async def webhook(request: Request):

    data = await request.json()
    print(data)

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]

        user_text = message["text"]["body"]
        user_number = message["from"]

        # dummy AI response (replace later with Gemini/OpenAI)
        ai_reply = f"You said: {user_text}"

        print("Reply to send:", ai_reply)

        return {"status": "ok"}

    except Exception as e:
        print("Error:", e)
        return {"status": "error"}