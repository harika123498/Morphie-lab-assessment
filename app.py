from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome! Go to <a href='/htop'>/htop</a> to see system information.</h1>"

@app.route('/htop')
def htop():
    # Get full name
    name = "P HARIKA"  # Replace with your full name

    # Get system username (alternative approach)
    username = os.environ.get("USER") or os.environ.get("USERNAME") or "Unknown User"

    # Get server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Get top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except subprocess.CalledProcessError as e:
        top_output = f"Error executing 'top' command: {e}"

    # Format the page content
    page_content = f"""
    <h1>System Info</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <h2>Top Output</h2>
    <pre>{top_output}</pre>
    """
    return page_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
