# Base Image
FROM debian:stable-slim

# Install needed programs
RUN apt-get update
RUN apt-get install -y python3

# Copy needed files
COPY main.py main.py
COPY books/ books/

# Run commands 
CMD ["python3", "main.py"]
