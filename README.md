# PYTHON-okex-OKX-Public-API-Buy-Limit-Monitor
OKX Public API Buy Limit Monitor PYTHON
# OKX Public API Buy Limit Monitor

This project is a Python script that monitors the buy limit (`buyLmt`) data for the `BTC-USD-SWAP` instrument from the OKX Public API. The script tracks the change rate of the buy limit over time and prints the change rate to the console every 10 seconds.

## Features
- Fetches `buyLmt` data every 3 seconds from OKX Public API.
- Tracks the change rate of `buyLmt` over time.
- Highlights the change rate in green for positive change and red for negative change.
- Runs indefinitely, printing data at regular intervals.

## Requirements
- Python 3.x
- `colorama` library for colored output in the terminal.

### Install dependencies:
To run this script, you need to install the following dependencies:
```bash
pip install colorama
