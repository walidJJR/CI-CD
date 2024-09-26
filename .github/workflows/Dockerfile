# Start with the FastAPI base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the current directory into the container's /app directory
COPY . /app

# Install the dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port 8001 where the app will run
EXPOSE 8001

# Uncomment the following lines if you have a .env file
# COPY .env /app
# Set environment variables from .env file
ENV ENV_FILE_LOCATION=/app/.env

# Command to run the FastAPI server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
