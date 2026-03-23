from flow_hunter.schemas.tick import Tick


class TickVelocity:
    def compute(self, ticks: list[Tick]) -> float:
        if len(ticks) < 2:
            return 0.0
        elapsed = ticks[-1].ts - ticks[0].ts
        if elapsed <= 0:
            return 0.0
        return len(ticks) / elapsed
