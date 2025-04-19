import re
import requests
import os

def is_valid_phone(phone: str) -> bool:
    return bool(re.match(r"^\+\d{10,15}$", phone))

def send_whatsapp_message(phone_number: str) -> bool:
    print("phone_number:", phone_number)
    
    phone_number_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID")  # Example: "110123456789012"
    token = os.getenv("WHATSAPP_TOKEN")  # Your actual Meta token
    
    url = f"https://graph.facebook.com/v18.0/{phone_number_id}/messages"
    
    payload = {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "text",
        "text": {"body": "Hello, this is a test message from our TMBC bot!"}
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print("Status code:", response.status_code)
    print("Response body:", response.text)
    
    return response.status_code == 200

