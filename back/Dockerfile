# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./back/requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 8080 for the Flask application
EXPOSE 8080

# Set the environment variable for Flask
ENV FLASK_APP=main.py

# Run the command to start the Flask application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8080"]
