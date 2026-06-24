# Cyberdeck System Monitor

A lightweight systems monitoring and observability tool, built on a Raspberry Pi.

---

## Why

I wanted to understand how real backend systems collect, store, and expose 
operational data, and build something hands-on that goes beyond tutorials.

---

## Architecture

| Layer | Tool | Purpose |
| --- | --- | --- |
| Metrics Collector | Python, psutil | Reads live CPU, memory, and disk stats |
| Storage Layer | SQLite | Stores readings with a timestamp |
| API Layer | FastAPI | Exposes metrics as JSON over HTTP |
| Clients | CLI / browser | Reads the data |

---

## Data Model

| Column | Type | Description |
| --- | --- | --- |
| id | INTEGER (primary key) | Auto-incrementing row ID |
| timestamp | TEXT | When the reading was taken |
| cpu_percent | REAL | CPU usage at time of reading |
| memory_percent | REAL | Memory usage at time of reading |
| disk_percent | REAL | Disk usage at time of reading |

---

## Status

- [x] Metrics collector (CPU, memory, disk)
- [x] SQLite persistence
- [x] FastAPI /metrics endpoint
- [x] /health endpoint
- [ ] /metrics/history (in progress)
- [ ] Future: alerting system
- [ ] Future: simple web dashboard
- [ ] Future: multi-device monitoring across network (not just this pi)

---

## Hardware

Running on a Raspberry Pi Zero 2 W, as part of a cyberdeck I'm building.

- Raspberry Pi Zero 2 W
- PiSugar battery (portable power)
- Waveshare 5-inch HDMI LCD screen
- Bluetooth keyboard
- microSD card
- GPIO header pins (ordered, need to connect the PiSugar battery)

Physical assembly: soldering the GPIO header, mounting the screen, and case/cable routing - still in progress.

---

## Tech Stack

- Python
- psutil
- SQLite
- FastAPI
- Uvicorn
- Raspberry Pi OS / Linux
