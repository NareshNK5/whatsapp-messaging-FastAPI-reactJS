from fastapi import FastAPI, Query, HTTPException
from utils import is_valid_phone, send_whatsapp_message
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/send_message")
def send_message(phone_number: str = Query(...)):
    if not is_valid_phone(phone_number):
        raise HTTPException(status_code=400, detail="Invalid phone number format")
    print("phone_number:",phone_number)
    success = send_whatsapp_message(phone_number)
    if not success:
        raise HTTPException(status_code=500, detail="Message could not be sent")
    
    return {"message": "Message sent successfully!"}
