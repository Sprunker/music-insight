# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install essential tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.10 \
    python3-pip \
    git \
    cmake \
    build-essential \
    libyaml-cpp-dev \
    libfftw3-dev \
    libavcodec-dev \
    libavformat-dev \
    libavutil-dev \
    libsamplerate0-dev \
    libtag1-dev \
    libchromaprint-dev \
    curl

# Install NumPy and TensorFlow with specific versions BEFORE essentia-tensorflow
RUN pip3 install numpy==1.21.6 tensorflow==2.11.0

# Install the required Python packages including essentia-tensorflow AFTER numpy and tensorflow
RUN pip3 install essentia-tensorflow
RUN pip3 install fastapi uvicorn requests python-multipart

# Create a working directory
WORKDIR /app

# Clone the GitHub repository (uncomment if necessary)
RUN git clone https://github.com/Sprunker/music-insight.git .
RUN ls -la  # Debug: Listar archivos

# Make sure that the 'download_test.sh' script is executable and run it
RUN chmod +x download_test.sh
RUN ./download_test.sh

# Expose the port that the application will run on
EXPOSE 8000

# Define the command to run your FastAPI application
CMD ["uvicorn", "music_insight_api:app", "--host", "0.0.0.0", "--port", "8000"]