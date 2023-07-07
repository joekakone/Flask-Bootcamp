#!/usr/bin/bash

# Stop container
docker stop cflaskapp

# Remove container 
docker rm cflaskapp

# Remove image
docker image rm iflaskapp:v1

# Build image
docker build -f Dockerfile -t iflaskapp:v1 .

# Run container
docker run -p 5000:5000 \
    --restart=always \
    -e FLASK_APP=app.py \
    --name cflaskapp \
    -d iflaskapp:v1
