# Use a lightweight Python base image compatible with AMD64 architecture
FROM --platform=linux/amd64 python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your application files into the container
COPY app.py .
COPY pdf_outline_extractor.py .

# Command to run your PDF processing script
CMD ["python", "app.py"]
