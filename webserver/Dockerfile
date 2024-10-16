# syntax=docker/dockerfile:1

FROM python:3.10-alpine
WORKDIR /app

# Copy the requirements file to use docker cache for dependencies layer
COPY requirements.txt requirements.txt

# Install build dependencies and Python requirements
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory into the container
COPY . .

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
EXPOSE 8080

# Run the application
CMD ["flask", "run", "--debug"]
