# FLOW HUNTER Next

This package adds a replay evaluator and metrics engine to the working FLOW HUNTER base.

## Run

```bash
export PYTHONPATH=src
python3 scripts/run_csv_replay.py
```

## What it does

- Reads sample CSV tick data
- Normalizes ticks
- Computes simple flow features
- Classifies regime and directional control
- Produces advisories
- Evaluates signals against forward price movement
- Prints performance metrics

## Expected output

A stream of advisories followed by a metrics block like:

```text
=== PERFORMANCE ===
{'total_trades': 3, 'wins': 2, 'losses': 1, 'win_rate': 0.67}
```
