from flask import Flask, request, jsonify, render_template_string
import sqlite3
import datetime

app = Flask(__name__)

# Create database table
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

# Track QR code scans
@app.route("/")
def track_scan():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
 yyy   cursor.execute("INSERT INTO scans (ip, user_agent, timestamp) VALUES (?, ?, ?)", (ip, user_agent, timestamp))
y    conn.commit()
    conn.close()

    return "✅ QR Code Tracking Active!"

# Display scan history in a simple web page
@app.route("/scans")
def view_scans():
    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, ip, user_agent, timestamp FROM scans ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()

    # Create a basic HTML table
    html = """
    <html>
    <head>
        <title>QR Code Scan History</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { width: 100%; border-collapse: collapse; }
            th, td { padding: 10px; border: 1px solid black; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h2>QR Code Scan History</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>IP Address</th>
                <th>Device Info</th>
                <th>Timestamp</th>
            </tr>
    """
    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"

    html += "</table></body></html>"

    return render_template_string(html)

if __name__ == "__main__":
    create_table()
    app.run(debug=True, host="0.0.0.0", port=10000)
from flask import Flask, request, jsonify, render_template_string
import sqlite3
import datetime

app = Flask(__name__)

# Create database table
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

# Track QR code scans
@app.route("/")
def track_scan():
    ip = request.remote_addr
    user_agent = request.headers.get("User-Agent")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scans (ip, user_agent, timestamp) VALUES (?, ?, ?)", (ip, user_agent, timestamp))
    conn.commit()
    conn.close()

    return "✅ QR Code Tracking Active!"

# Display scan history in a simple web page
@app.route("/scans")
def view_scans():
    conn = sqlite3.connect("scans.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, ip, user_agent, timestamp FROM scans ORDER BY timestamp DESC")
    data = cursor.fetchall()
    conn.close()

    # Create a basic HTML table
    html = """
    <html>
    <head>
        <title>QR Code Scan History</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { width: 100%; border-collapse: collapse; }
            th, td { padding: 10px; border: 1px solid black; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h2>QR Code Scan History</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>IP Address</th>
                <th>Device Info</th>
                <th>Timestamp</th>
            </tr>
    """
    for row in data:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>"

    html += "</table></body></html>"

    return render_template_string(html)

if __name__ == "__main__":
    create_table()
    app.run(debug=True)from flask import Flask, request, jsonify, render_template
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
    app.run(debug=True, host="0.0.0.0", port=10000)
