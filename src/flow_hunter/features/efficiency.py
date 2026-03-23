from flow_hunter.schemas.tick import Tick


class Efficiency:
    def compute(self, ticks: list[Tick]) -> float:
        if len(ticks) < 2:
            return 0.0
        total_abs_move = sum(abs(t.mid_delta_pips) for t in ticks[1:])
        if total_abs_move <= 0:
            return 0.0

        pair = ticks[-1].pair
        m = 100.0 if "JPY" in pair else 10000.0
        net_move = abs(ticks[-1].mid - ticks[0].mid) * m
        return min(net_move / total_abs_move, 1.0)
