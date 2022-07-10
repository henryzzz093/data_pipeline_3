# Dockerfile, Image, Container

# Build an image starting with the Python 3.7 image
FROM python:3.7  

# Set the working directory to /app
WORKDIR /app

# Set environment variables 
ENV PYTHONPATH "${PYTHONPATH}:/app/plugins/"
ENV PYTHONPATH "${PYTHONPATH}:/app/"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt