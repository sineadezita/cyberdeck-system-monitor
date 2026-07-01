import psutil
from database import init_db, save_metrics

def get_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
    }

if __name__ == "__main__":
    init_db()
    data = get_metrics()
    save_metrics(data)
    print("Saved:", data)


def check_alerts(data, cpu_threshold=80, memory_threshold=80, disk_threshold=90):
    alerts = []
    if data["cpu_percent"] >= cpu_threshold:
        alerts.append(f"High CPU usage: {data['cpu_percent']}%")
    if data["memory_percent"] >= memory_threshold:
        alerts.append(f"High memory usage: {data['memory_percent']}%")
    if data["disk_percent"] >= disk_threshold:
        alerts.append(f"High disk usage: {data['disk_percent']}%")
    return alerts
