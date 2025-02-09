from flask import Flask, request

import sqlite3
import datetime

app = Flask(__name__)

# Function to log the scan
def log_scan(ip, user_agent):
    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scans (id INTEGER PRIMARY KEY, ip TEXT, user_agent TEXT, timestamp TEXT)")
    cursor.execute("INSERT INTO scans (ip, user_agent, timestamp) VALUES (?, ?, ?)",
                   (ip, user_agent, datetime.datetime.now()))
    conn.commit()
    conn.close()

@app.route("/")
def home():
    ip = request.remote_addr  # Get visitor's IP
    user_agent = request.headers.get("User-Agent")  # Get device info
    log_scan(ip, user_agent)  # Log the scan
    return "<h1>Welcome! Your scan has been recorded.</h1>"

@app.route("/logs")
def show_logs():
    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans")
    logs = cursor.fetchall()
    conn.close()

    html = "<h1>Scan Logs</h1><table border='1'><tr><th>ID</th><th>IP</th><th>Device</th><th>Time</th></tr>"
    for log in logs:
        html += f"<tr><td>{log[0]}</td><td>{log[1]}</td><td>{log[2]}</td><td>{log[3]}</td></tr>"
    html += "</table>"

    return html

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Use port 5000 locally, otherwise get from env
    app.run(host="0.0.0.0", port=port)
    
