import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("metrics.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            cpu_percent REAL,
            memory_percent REAL,
            disk_percent REAL
        )
    """)
    conn.commit()
    conn.close()


def save_metrics(data):
    conn = sqlite3.connect("metrics.db")
    conn.execute("""
        INSERT INTO metrics (timestamp, cpu_percent, memory_percent, disk_percent)
        VALUES (?, ?, ?, ?)
    """, (datetime.now().isoformat(), data["cpu_percent"], data["memory_percent"], data["disk_percent"]))
    conn.commit()
    conn.close()
