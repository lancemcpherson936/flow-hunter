from collections import deque

from flow_hunter.schemas.tick import Tick


class TickBuffer:
    def __init__(self, maxlen: int = 500) -> None:
        self._ticks: deque[Tick] = deque(maxlen=maxlen)

    def append(self, tick: Tick) -> None:
        self._ticks.append(tick)

    def last_n(self, n: int) -> list[Tick]:
        if n <= 0:
            return []
        return list(self._ticks)[-n:]

    def __len__(self) -> int:
        return len(self._ticks)
