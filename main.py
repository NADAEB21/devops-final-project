from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Book Inventory API")

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
    return {"message": "Welcome to the DevOps Project API!"}