from flow_hunter.schemas.tick import Tick


class DirectionalImbalance:
    def compute(self, ticks: list[Tick]) -> float:
        if not ticks:
            return 0.0
        up = sum(1 for t in ticks if t.mid_delta_pips > 0)
        down = sum(1 for t in ticks if t.mid_delta_pips < 0)
        total = up + down
        if total == 0:
            return 0.0
        return (up - down) / total
