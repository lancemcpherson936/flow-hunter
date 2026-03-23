from flow_hunter.schemas.tick import Tick


class QuoteAsymmetry:
    def compute(self, ticks: list[Tick]) -> float:
        if not ticks:
            return 0.0
        bid_up = sum(1 for t in ticks if t.bid_delta_pips > 0)
        ask_down = sum(1 for t in ticks if t.ask_delta_pips < 0)
        total = len(ticks)
        return (bid_up - ask_down) / total if total else 0.0
