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
