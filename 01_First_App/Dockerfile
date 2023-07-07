# Base Docker Image
FROM python:3-buster

# Set Working directory
WORKDIR /app

# Copy source code in the container
ADD . /app

# Install dependencies
RUN pip install --upgrade pip \
	&& pip install -r requirements.txt

# Enable access to the port
EXPOSE 5000

# Launch application
CMD ["python", "app.py", "--debug", "--host=0.0.0.0", "--port=5000"]
