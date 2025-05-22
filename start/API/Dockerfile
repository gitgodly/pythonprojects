# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (change if using another)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
