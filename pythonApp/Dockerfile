# Use official Python image as base
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create logs directory
RUN mkdir -p host_logs

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]