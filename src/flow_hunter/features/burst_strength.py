from flow_hunter.schemas.tick import Tick


class BurstStrength:
    def compute(self, ticks: list[Tick]) -> float:
        if len(ticks) < 3:
            return 0.0

        best = 0.0
        current_dir = 0
        streak = 0
        displacement = 0.0

        for t in ticks:
            direction = 1 if t.mid_delta_pips > 0 else -1 if t.mid_delta_pips < 0 else 0
            if direction == 0:
                continue

            if direction == current_dir:
                streak += 1
                displacement += abs(t.mid_delta_pips)
            else:
                current_dir = direction
                streak = 1
                displacement = abs(t.mid_delta_pips)

            score = min((streak / 8.0) + (displacement / 4.0), 1.0)
            if score > best:
                best = score

        return best
