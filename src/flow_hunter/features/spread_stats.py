from statistics import mean, pstdev

from flow_hunter.schemas.tick import Tick


class SpreadStats:
    def compute(self, ticks: list[Tick]) -> tuple[float, float]:
        if not ticks:
            return 0.0, 0.0
        spreads = [t.spread_pips for t in ticks]
        if len(spreads) == 1:
            return spreads[0], 0.0
        return mean(spreads), pstdev(spreads)
