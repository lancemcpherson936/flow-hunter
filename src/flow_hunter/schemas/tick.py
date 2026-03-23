from dataclasses import dataclass


@dataclass(slots=True)
class Tick:
    ts: float
    pair: str
    bid: float
    ask: float
    mid: float
    spread_pips: float
    bid_delta_pips: float
    ask_delta_pips: float
    mid_delta_pips: float
    dt_ms: int
