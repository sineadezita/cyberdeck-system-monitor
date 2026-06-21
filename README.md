# Cyberdeck System Monitor

A lightweight systems monitoring and observability tool, built on a Raspberry Pi.

## Why

I wanted to understand how real backend systems collect, store, and expose 
operational data, and build something hands-on that goes beyond tutorials.

## Architecture

| Layer | Tool | Purpose |
| --- | --- | --- |
| Metrics Collector | Python, psutil | Reads live CPU, memory, and disk stats |
| Storage Layer | SQLite | Saves readings with a timestamp |
| API Layer | FastAPI | Exposes metrics as JSON over HTTP |
| Clients | CLI / browser | Reads the data |

## Status

- [x] Metrics collector (CPU, memory, disk)
- [ ] SQLite persistence
- [ ] FastAPI /metrics endpoint
- [ ] /health endpoint
- [ ] Future: alerting, simple web dashboard

## Hardware

Running on a Raspberry Pi Zero 2 W, as part of a cyberdeck I'm building.

- Raspberry Pi Zero 2 W
- PiSugar battery (portable power)
- Waveshare 5-inch HDMI LCD screen
- Bluetooth keyboard
- microSD card
- GPIO header pins (ordered, neede to connect the PiSugar battery)

Physical assembly - soldering the GPIO header, mounting the screen, and case/cable routint - still in progress.


## Tech

Python, psutil, SQLite, FastAPI
