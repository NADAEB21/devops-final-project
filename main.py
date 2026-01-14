from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from prometheus_fastapi_instrumentator import Instrumentator
import logging
from pythonjsonlogger import jsonlogger

app = FastAPI(title="Book Inventory API")
# Configuration des logs en JSON
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)
logger.info("Démarrage de l'application DevOps", extra={"version": "1.0", "env": "dev"})
# Configuration de l'instrumentation Prometheus
Instrumentator().instrument(app).expose(app)

# A simple "Database" in memory
inventory = []

# The 'Schema' - what a Book looks like
class Book(BaseModel):
    id: int
    title: str
    author: str

# 1. Health Check Endpoint (Essential for DevOps/Kubernetes later)
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# 2. Get all books
@app.get("/books", response_model=List[Book])
def get_books():
    return inventory

# 3. Add a book
@app.post("/books", status_code=201)
def add_book(book: Book):
    inventory.append(book)
    return {"message": f"Book '{book.title}' added successfully!"}

# Root endpoint
@app.get("/")
def read_root():
    # C'est ici qu'on déclenche le log JSON
    logger.info("Accès à la page d'accueil", extra={"user": "admin", "action": "visit"})
    return {"message": "Hello DevOps"}


