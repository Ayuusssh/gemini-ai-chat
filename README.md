# 🤖 Gemini AI Chat

**Gemini AI Chat** is a **Python-based chatbot** powered by **Google's Gemini API**.  
It allows you to interact with **Gemini 2.0 Flash** in real-time while keeping your API key **secure** using `.env` or **OS environment variables**.

---

## 🚀 Features
- 💬 Real-time chat with **Google Gemini AI**
- 🔒 Secure API key handling via `.env`
- ⚡ Lightweight and beginner-friendly
- 🌎 Works on **Windows**, **Linux**, and **macOS**
- 🧩 Fully customizable Python implementation

---

## 📌 Getting Started

Follow these steps to set up and run the chatbot:

---

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ayush-bhavsar/gemini-ai-chat.git
cd gemini-ai-chat
````

---

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

**requirements.txt**

```txt
google-generativeai
python-dotenv
```

---

### **3️⃣ Get Your Google Gemini API Key**

1. Go to **[Google AI Studio](https://aistudio.google.com/app/apikey)**.
2. Sign in with your Google account.
3. Click **"Create API Key"**.
4. Copy your API key.

---

### **4️⃣ Add Your API Key**

#### **Option 1 — Using `.env` (Recommended)**

Create a `.env` file in the root directory and add:

```env
GOOGLE_API_KEY=your_api_key_here
```

> ⚠️ `.env` is already ignored via `.gitignore` to keep your key safe.

#### **Option 2 — Using OS Environment Variables**

* **Windows:**

  ```bash
  setx GOOGLE_API_KEY "your_api_key_here"
  ```
* **macOS/Linux:**

  ```bash
  export GOOGLE_API_KEY="your_api_key_here"
  ```

---

### **5️⃣ Run the Chatbot**

```bash
python gemini-chatbot.py
```

**Example Output:**

```
Welcome to the chat! Type 'exit' to quit.
You: Hello Gemini!
Gemini: Hi there! How can I assist you today? 😊
You: exit
Exiting the chat. Goodbye!
```

---

## 📂 Project Structure

```
gemini-ai-chat/
│── main.py             # Main chatbot script
│── requirements.txt    # Python dependencies
│── .env                # Stores your API key (ignored by git)
│── .gitignore          # Keeps sensitive files safe
└── README.md           # Project documentation
```

---

## 🔐 Security Best Practices

* ❌ **Do not** hardcode your API key in `gemini-chatbot.py`
* ✅ Use `.env` or **OS environment variables**
* ✅ Keep `.env` in `.gitignore`

---

## 📚 Resources

* [Google AI Studio](https://aistudio.google.com/app/apikey)
* [Gemini API Documentation](https://ai.google.dev/docs)
* [Python Docs](https://docs.python.org/3/)

---


## 👨‍💻 Author
**Ayush Bhavsar**
📧 [Ayush Bhavsar](mailto:ayushbhavsar1402@gmail.com)

<p align="center">Made with ❤️ using Python and Google Gemini API</p>
```
