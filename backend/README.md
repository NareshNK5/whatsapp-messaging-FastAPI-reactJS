# 📡 WhatsApp Messaging Backend (FastAPI)

This is a simple FastAPI backend service that allows sending WhatsApp messages via Meta's WhatsApp Cloud API.

---

## 🚀 Endpoint


---

## 🛠️ Features

- Phone number validation (E.164 format)
- Message sending via WhatsApp Cloud API
- CORS enabled for frontend (React)
- `.env` support for secure credentials

---

## 📦 Tech Stack

- Python 3.10+
- FastAPI
- `python-dotenv`
- `requests`

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` folder:

```env
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id_here
WHATSAPP_TOKEN=your_meta_access_token

cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
