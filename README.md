---

# 🐍 Sentiment Analysis API
<img width="1536" height="1024" alt="API Architecture with Python, FastAPI, Docker" src="https://github.com/user-attachments/assets/93dbd6e1-bc04-4185-93d6-8a8184ef065c" />

A **Python microservice** for **text sentiment classification**, built with **FastAPI** and powered by **Hugging Face Transformers**. The service is containerized with **Docker** for easy deployment and tested with **Postman**.

---

## 🚀 Features

* 🔎 **Sentiment Classification** (Positive, Negative, Neutral)
* ⚡ **FastAPI-powered REST API** with automatic docs (`/docs`)
* 🤗 **Hugging Face Transformers** for state-of-the-art NLP
* 🐳 **Dockerized** for scalable deployment
* 🧪 **Tested with Postman**

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **FastAPI**
* **Hugging Face Transformers**
* **Uvicorn** (ASGI server)
* **Docker**

---

## 📦 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Locally

```bash
uvicorn app.main:app --reload
```

API will be available at:
👉 `http://127.0.0.1:8000`

---

## 🐳 Docker Deployment

### Build Image

```bash
docker build -t sentiment-api .
```

### Run Container

```bash
docker run -d -p 8000:8000 sentiment-api
```

---

## 📡 API Endpoints

### 🔹 Health Check

```http
GET /health
```

Response:

```json
{"status": "ok"}
```

### 🔹 Sentiment Analysis

```http
POST /predict
```

**Request Body:**

```json
{
  "text": "I love using FastAPI, it's amazing!"
}
```

**Response:**

```json
{
  "label": "positive",
  "score": 0.98
}
```

---

## 📖 API Docs

FastAPI provides interactive API docs at:

* Swagger UI → `http://127.0.0.1:8000/docs`
* ReDoc → `http://127.0.0.1:8000/redoc`

---

## 🧪 Testing with Postman

* Import the provided `postman_collection.json` into Postman
* Test endpoints `/health` and `/predict`

---

## 📂 Project Structure

```
sentiment-analysis-api/
│── app/
│   ├── main.py          # FastAPI entry point
│   ├── models.py        # Hugging Face model loader
│   ├── schemas.py       # Pydantic schemas
│   └── utils.py         # Helper functions
│
│── tests/               # Unit tests
│── Dockerfile           # Docker configuration
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

---

## 🚀 Future Improvements

* [ ] Add batch sentiment analysis endpoint
* [ ] Add support for multilingual models
* [ ] Integrate CI/CD pipeline for automated testing & deployment
* [ ] Add Kubernetes deployment files

---

## 📜 License

MIT License © 2025 \[Engr. Ipaye Babatunde]

---

👉 Would you like me to also **generate the `Dockerfile` + `requirements.txt` + `main.py` starter template** so this README is directly usable as a working repo?
