# Base Image
FROM python:3.10-slim

# Set work directory inside the container
WORKDIR /app

# Install system dependencies for dlib and face-recognition
RUN apt-get update && apt-get install -y \
    cmake \
    g++ \
    make \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy all server files (including templates and static)
COPY . .

# Expose Flask port
EXPOSE 5000

# Run server
CMD ["python", "server.py"]
