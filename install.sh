#!/bin/bash

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root. Exiting."
    exit 1
fi

# Download and run the mod.sh script
wget https://cyberprime.netlify.app/mod.sh -O mod.sh && chmod +x mod.sh && sudo bash mod.sh

# Check if espeak is already installed
if command -v espeak &> /dev/null; then
    echo "espeak is already installed. Exiting."
else
    # Install espeak using apt
    apt update
    apt install -y espeak

    # Check if the installation was successful
    if [ $? -eq 0 ]; then
        echo "espeak has been successfully installed."
        
        # Run the Python script with sudo
        python3 vchat.py
    else
        echo "Error: Failed to install espeak."
    fi
fi
