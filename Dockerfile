# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy your application code to the container
COPY . /app

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
