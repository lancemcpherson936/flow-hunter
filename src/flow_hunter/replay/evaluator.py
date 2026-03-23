from dataclasses import dataclass


@dataclass
class TradeResult:
    entry_price: float
    direction: str
    max_favorable: float = 0.0
    max_adverse: float = 0.0
    outcome: str = "open"


class ReplayEvaluator:
    def __init__(self, target_pips: float = 5.0, stop_pips: float = 5.0):
        self.target = target_pips
        self.stop = stop_pips
        self.active_trade: TradeResult | None = None
        self.results: list[TradeResult] = []

    def on_signal(self, price: float, direction: str) -> None:
        if self.active_trade is None:
            self.active_trade = TradeResult(price, direction)

    def on_tick(self, price: float) -> None:
        if not self.active_trade:
            return

        trade = self.active_trade
        move = (price - trade.entry_price) * 10000

        if trade.direction == "short":
            move *= -1

        trade.max_favorable = max(trade.max_favorable, move)
        trade.max_adverse = min(trade.max_adverse, move)

        if move >= self.target:
            trade.outcome = "win"
            self.results.append(trade)
            self.active_trade = None
        elif move <= -self.stop:
            trade.outcome = "loss"
            self.results.append(trade)
            self.active_trade = None
