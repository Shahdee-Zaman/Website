# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY main.py .
COPY app/ app/

# Expose port for Flask
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
