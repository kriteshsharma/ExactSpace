# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Create a virtual environment
RUN python3 -m venv myenv

# Activate the virtual environment
SHELL ["bash", "-c"]
RUN source myenv/bin/activate

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "main.py"]
