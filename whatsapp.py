import requests
import os


ACCESS_TOKEN = os.getenv("EAGEG6JRYI5ABRymoS2xSSnNfajU0Nw7OWokwZAwUwGApVNfQolj382sNZCrmJKxSZBtQXdIJ5iMvoWdAN8XCpovUU7O503MsBqqnPgYVFqZAeDZBXVAH6qBmuNS28GOk8mXqL39pxuPPZCGaVpVifi9Ih8PgLnQEfr8zrPZAtVvgJP1m9e35f4ZAi5XPyZBJ7E8ALL9siKh0ZBDmDoeX5V6myuMNrSKIj4D64nZBMNHrItYduWZCGXadZBEOgXJLMULJUVhdpUlpevShelexCzdj9vZCZAk")
PHONE_NUMBER_ID = os.getenv("1196533463550821")


def send_whatsapp_message(to, message):

    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"


    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }


    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }


    response = requests.post(url, headers=headers, json=data)

    return response.json()