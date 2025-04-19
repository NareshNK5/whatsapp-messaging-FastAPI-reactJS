# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.



---

## 📁 `frontend/README.md` (React.js)

```markdown
# 💬 WhatsApp Messaging Frontend (React.js)

This is a simple React-based frontend that lets you send a WhatsApp message to any phone number using the FastAPI backend.

---

## 🧩 Features

- Phone number input form
- Message status feedback
- Axios integration with backend
- Vite-powered React setup

---

## 📦 Tech Stack

- React (Vite)
- Axios

---

## 📥 Installation

```bash
cd frontend
npm install


npm run dev


http://localhost:8000/send_message?phone_number=<number>
