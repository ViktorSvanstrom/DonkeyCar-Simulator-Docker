FROM ubuntu:22.04

# Install necessary packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    libfontconfig1 \
    libice6 \
    libx11-6 \
    libxau6 \
    libxdmcp6 \
    libxcb1 \
    libxss1 \
    libgconf-2-4 \
    libxtst6 \
    libxrandr2 \
    libasound2 \
    libpangocairo-1.0-0 \
    libatk1.0-0 \
    libcairo-gobject2 \
    libgtk-3-0 \
    libgdk-pixbuf2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Download DonkeySimLinux.zip
RUN wget https://github.com/tawnkramer/gym-donkeycar/releases/download/v22.11.06/DonkeySimLinux.zip

# Extract the zip file
RUN unzip DonkeySimLinux.zip -d DonkeySimLinux

# Change to the extracted directory
WORKDIR /app/DonkeySimLinux

# Navigate to the inner DonkeySimLinux directory
WORKDIR /app/DonkeySimLinux/DonkeySimLinux

# Make the simulator executable
RUN chmod +x donkey_sim.x86_64

# Run the simulator
CMD ["./donkey_sim.x86_64"]
