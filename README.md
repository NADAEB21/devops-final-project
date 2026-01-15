# DevOps Final Project: Book Inventory API

## Overview
This project is a small backend service designed to demonstrate end-to-end DevOps concepts. It features a REST API built with **FastAPI**, fully containerized with **Docker**, monitored with **Prometheus**, and orchestrated via **Kubernetes**.

The entire lifecycle is managed through a **CI/CD pipeline** that includes automated testing and security scanning.

## 🚀 Features
- **Backend:** Python FastAPI implementation (under 150 lines).
- **CI/CD:** Automated testing and SAST scanning via GitHub Actions.
- **Containerization:** Optimized Docker image using `python:3.13-slim`.
- **Observability:** 
  - **Metrics:** Prometheus endpoint at `/metrics`.
  - **Logging:** Structured JSON logging for production readiness.
- **Security:** Static (Bandit) and Dynamic (OWASP ZAP) security testing.
- **Orchestration:** Kubernetes Deployment (2 replicas) and NodePort Service.

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Framework:** FastAPI
- **Tools:** Docker, Kubernetes (Minikube), GitHub Actions, Pytest, Bandit, OWASP ZAP.

---

## 💻 Local Setup & Running

### 1. Prerequisites
- Python 3.13+
- Docker Desktop
- Minikube & Kubectl

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/NADAEB21/devops-final-project.git
cd devops-final-project

# Create and activate virtual environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```
### 3. Running the API
```bash
uvicorn main:app --reload

```
The API will be available at http://127.0.0.1:8000
### 🐳 Docker Usage
```bash
# Build the image
docker build -t inventory-app .

# Run the container
docker run -d -p 8000:8000 --name inventory-api inventory-app

```
### ☸️ Kubernetes Deployment
```bash
# Start minikube
minikube start

# Use minikube's docker daemon
minikube docker-env | Invoke-Expression

# Build image inside minikube
docker build -t inventory-app .

# Apply manifests
kubectl apply -f kubernetes/

# Access the service
minikube service devops-api-service --url

```
### 📊 API Endpoints & Observability
**Root:** GET / - Welcome message.
**Health Check:** GET /health - Service status.
**Metrics:** GET /metrics - Prometheus metrics.
**API Docs:** GET /docs - Interactive Swagger UI.

### 🛡️ Security
**SAST:** Automated Bandit scans run on every push via GitHub Actions.
**DAST:** Manual OWASP ZAP scans are performed on the running Docker container.