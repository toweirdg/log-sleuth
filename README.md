# Log Intelligence Engine 🚀

AI-powered backend system for analyzing logs, detecting anomalies, and generating actionable insights using asynchronous processing.

---

## 🧠 Problem

Modern distributed systems generate massive volumes of logs, making it difficult to:

* Detect issues in real-time
* Identify root causes quickly
* Prevent failures before escalation

---

## 💡 Solution

This project implements a scalable backend system that:

* Ingests logs via REST API
* Stores logs in PostgreSQL
* Processes logs asynchronously using Celery + Redis
* Analyzes logs using rule-based + AI-inspired logic  
* Generates insights and recommended actions
  
---

## 🚀 Demo Flow

1. `POST /logs` → Submit log  
2. Background worker processes log asynchronously  
3. AI engine generates insight + action  
4. `GET /logs/{id}` → Retrieve processed result  
5. `GET /logs/stats` → View aggregated system metrics  

---

## ⚙️ Features

* FastAPI backend with RESTful design  
* PostgreSQL integration with SQLAlchemy ORM  
* Asynchronous processing using Celery + Redis  
* Rule-based + AI-inspired log analysis engine  
* Automated decision engine for system actions  
* Log analytics endpoint (`/logs/stats`)  
* Dockerized services for reproducible setup 

---

## 🏗️ Architecture (Current)

Client 
   ⟶
FastAPI (API Layer) 
   ⟶ 
PostgreSQL (Storage) 
   ⟶
Redis (Message Broker) 
   ⟶
Celery Worker (Processing + AI Engine)

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
* Docker
* Git & GitHub

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
REDIS_URL=redis://localhost:6379/0

---

### 5. Run Services

* Start Redis
 --redis-server.exe
* Start FastAPI
 --uvicorn app.main:app --reload
* Start Celery Worker(Windows Fix)
 --celery -A app.workers.celery_app worker --pool=solo --loglevel=info

---

## 🧪 API Example

### Create Log

```http
POST /logs
  "message": "Database connection timeout error",
  "level": "ERROR"
}

### 📊 Sample Output
{
  "id": 1,
  "status": "processed_error",
  "pattern": ["timeout"],
  "action": "Restart service / check load",
  "analysis": "Issue detected: timeout. Likely system instability."
}
```
---
### 🚧 Future Improvements:
* LLM integration (local models like Ollama)
* Advanced anomaly detection
* Root cause analysis engine
* Alerting & notification system
* Role-based authentication (JWT)
 
---
## 👨‍💻 Author

Gulshan Kumar

