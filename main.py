from fastapi import FastAPI
from collector import get_metrics
from database import init_db, save_metrics

app = FastAPI()

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
