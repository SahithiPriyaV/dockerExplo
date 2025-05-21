import os
import logging
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# Get HOSTNAME from environment (Docker sets this to the container ID)
hostname = os.getenv('HOSTNAME', 'unknown')

# Set log directory and ensure it exists
log_dir = '/logs'
os.makedirs(log_dir, exist_ok=True)

# Construct log file path
log_file_path = f'{log_dir}/app.log'

# Configure logging with HOSTNAME in the format
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format=f'%(asctime)s - %(levelname)s - HOSTNAME={hostname} - %(message)s'
)

@app.route('/')
def home():
    return "himshello from Flask inside Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
