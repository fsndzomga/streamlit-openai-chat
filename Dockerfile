# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt first, then the rest of the code (better for caching)
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose ports: 8000 for FastAPI, 8501 for Streamlit
EXPOSE 8000 8501

# Run both FastAPI and Streamlit using a script or supervisor (to run multiple processes)
CMD ["./run.sh"]
