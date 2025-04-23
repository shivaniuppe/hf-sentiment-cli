# 💬 Hugging Face Sentiment Analysis Web App

A lightweight web app that performs real-time sentiment analysis on user-entered text using Hugging Face Transformers. Built with Flask and the `transformers` pipeline, it classifies input as **Positive** or **Negative** with confidence scores.

---

## 🚀 Features

- Real-time sentiment analysis via web interface
- Uses Hugging Face’s `distilbert-base-uncased-finetuned-sst-2-english` model
- Built with Python Flask
- Clean UI with separate `styles.css`

---

## 🧠 Tech Stack

- **Frontend**: HTML, CSS (via `static/styles.css`)
- **Backend**: Python Flask
- **NLP Engine**: Hugging Face Transformers (`pipeline` API)

---

## 🧰 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/shivaniuppe/hf-sentiment-web.git
cd hf-sentiment-web
```

### 2. Set up your environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## 📂 Project Structure

```
hf-sentiment-web/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── requirements.txt
└── README.md
```

---

## 🧪 Example Input

> "I absolutely love working with AI tools like this one!"

🧠 **Output:**
- **Sentiment:** POSITIVE
- **Confidence:** 99.82%

---


## 👩‍💻 Author

**Shivani Uppe**  
Master of Applied Computer Science – Dalhousie University  
[LinkedIn](https://www.linkedin.com/in/shivaniuppe) | [GitHub](https://github.com/shivaniuppe)
