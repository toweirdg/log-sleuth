# Log Intelligence Engine 🚀

AI-powered backend system to analyze logs, detect anomalies, and automate operational decisions using asynchronous processing and AI.

---

## 🧠 Problem

Modern systems generate massive volumes of logs. Engineers often struggle to:

* Detect issues in real-time
* Identify root causes quickly
* Prevent downtime before escalates

---

## 💡 Solution

This project provides a scalable backend that:

* Ingests logs via API
* Stores them in PostgreSQL
* Processes logs asynchronously using Celery + Redis
* Prepares logs for AI-based analysis and decision-making

---

## ⚙️ Current Features (Phase 1–3)

* ✅ FastAPI backend
* ✅ PostgreSQL integration
* ✅ Log ingestion API (`/logs`)
* ✅ SQLAlchemy ORM models
* ✅ Asynchronous processing using Celery + Redis
* ✅ Background task execution for log analysis
* ✅ Rule-based + AI-like log analysis engine
* ✅ Automated decision engine for system actions
* ✅Scalable backedn architecture

---

## 🏗️ Architecture (Current)

Client 
   ↓
FastAPI (API Layer) 
   ↓ 
PostgreSQL (Storage) 
   ↓ 
Redis (Queue) 
   ↓ 
Celery Worker (Processing)

---

### 🛠️ Tech Stack

##Core Backend
* Python
* FastAPI
* SQLAlchemy

##Database
* PostgreSQL

##Async Processing
* Redis (message broker)
* Celery (background worker)

##Dev Tools
* Git & GitHub

---

## 🚧 Upcoming Features

* AI-powered log analysis (LLM integration)
* Root cause detection
* Anomally detection system
* Automated decision engine (self-healing action)
* Alerting system 

---

## Setup Instructions

### 1. Clone the Repository


git clone https://github.com/toweirdg/log-intelligence-engine.git
cd log-intelligence-engine

### 2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows 

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Environment Variables

Create a `.env` file in the root directory and configure the following:


DATABASE_URL=postgresql://username:password@localhost:5432/log_engine
OPENAI_API_KEY=your_api_key_here
REDIS_URL=redis://localhost:6379/0

---

### 5. Start Services

* Start Redis
 --redis-server.exe
* Start FastAPI
 --uvicorn app.main:app --reload
* Start Celery Worker(Windows Fix)
 --celery -A app.workers.celery_app worker --pool=solo --loglevel=info

---

###🧪 API Usage
POST /logs
{
  "message": "Database connection error",
  "level": "ERROR"
}

---
## 📌 Author

Gulshan Kumar

