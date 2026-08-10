from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from collector import get_metrics, check_alerts
from database import init_db, save_metrics, get_history

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
def startup():
    init_db()


@app.get("/metrics")
def read_metrics():
    data = get_metrics()
    save_metrics(data)
    return data


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/metrics/history")
def read_history():
    return get_history()


@app.get("/alerts")
def read_alerts():
    data = get_metrics()
    return {"alerts": check_alerts(data)}
