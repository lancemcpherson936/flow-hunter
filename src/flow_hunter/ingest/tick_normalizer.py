from flow_hunter.schemas.tick import Tick


class TickNormalizer:
    def __init__(self) -> None:
        self._last_bid: float | None = None
        self._last_ask: float | None = None
        self._last_ts: float | None = None

    @staticmethod
    def _pip_multiplier(pair: str) -> float:
        return 100.0 if "JPY" in pair else 10000.0

    def normalize(self, raw: dict) -> Tick:
        pair = str(raw["pair"])
        ts = float(raw["ts"])
        bid = float(raw["bid"])
        ask = float(raw["ask"])
        mid = (bid + ask) / 2.0
        m = self._pip_multiplier(pair)

        if self._last_bid is None or self._last_ask is None or self._last_ts is None:
            bid_delta = 0.0
            ask_delta = 0.0
            mid_delta = 0.0
            dt_ms = 0
        else:
            last_mid = (self._last_bid + self._last_ask) / 2.0
            bid_delta = (bid - self._last_bid) * m
            ask_delta = (ask - self._last_ask) * m
            mid_delta = (mid - last_mid) * m
            dt_ms = max(int((ts - self._last_ts) * 1000), 0)

        spread_pips = (ask - bid) * m
        self._last_bid = bid
        self._last_ask = ask
        self._last_ts = ts

        return Tick(
            ts=ts,
            pair=pair,
            bid=bid,
            ask=ask,
            mid=mid,
            spread_pips=spread_pips,
            bid_delta_pips=bid_delta,
            ask_delta_pips=ask_delta,
            mid_delta_pips=mid_delta,
            dt_ms=dt_ms,
        )
