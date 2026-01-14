# 1. Use an official Python base image (The "mini-Linux" with Python)
FROM python:3.13-slim

# 2. Set the "working directory" inside the container
WORKDIR /app

# 3. Copy only the requirements file first (Optimization trick)
COPY requirements.txt .

# 4. Install the dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code
COPY . .

# 6. Tell the container which port to open
EXPOSE 8000

# 7. The command to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]