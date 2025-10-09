# Base image
FROM debian:stable-slim

# Copy source destination
COPY lab /bin/goserver

# Enviroment
ENV PORT=8991

# Start the server
CMD ["/bin/goserver"]
