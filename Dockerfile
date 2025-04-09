# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (including git)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the src directory and requirements.txt into the container
COPY discord-bot/src /app/src
COPY requirements.txt /app/

# Install pip and upgrade it
RUN pip install --no-cache-dir --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH to include /app
ENV PYTHONPATH=/app

# Expose port (optional, if needed for debugging or HTTP servers)
EXPOSE 8000

# Run the bot
CMD ["python", "src/main.py"]