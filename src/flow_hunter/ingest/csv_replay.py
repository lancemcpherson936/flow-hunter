import csv
from pathlib import Path


class CSVReplayReader:
    def __init__(self, path: str) -> None:
        self.path = Path(path)

    def read(self) -> list[dict]:
        rows: list[dict] = []
        with self.path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(
                    {
                        "ts": float(row["ts"]),
                        "pair": row["pair"],
                        "bid": float(row["bid"]),
                        "ask": float(row["ask"]),
                    }
                )
        return rows
