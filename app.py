from flask import Flask, request, jsonify, render_template
import sqlite3
import datetime

app = Flask(__name__)

# Create a database table for scans
def create_table():
    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            user_agent TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Track each scan
@app.route("/")
def track_scan():
    ip = request.remote_addr  # Get visitor's IP
    user_agent = request.headers.get("User-Agent")  # Get device info
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Store in database
    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scans (ip, user_agent, timestamp) VALUES (?, ?, ?)", (ip, user_agent, timestamp))
    conn.commit()
    conn.close()

    return "✅ Scan recorded! Thank you for visiting!"

# View scan history
@app.route("/scans")
def view_scans():
    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    create_table()
    app.run(debug=True)
