class Metrics:
    def compute(self, results):
        if not results:
            return {
                "total_trades": 0,
                "wins": 0,
                "losses": 0,
                "win_rate": 0.0,
                "avg_win_pips": 0.0,
                "avg_loss_pips": 0.0,
            }

        wins = sum(1 for r in results if r.outcome == "win")
        losses = sum(1 for r in results if r.outcome == "loss")
        total = len(results)
        win_rate = wins / total if total else 0

        avg_win = sum(r.max_favorable for r in results if r.outcome == "win") / max(wins, 1)
        avg_loss = sum(abs(r.max_adverse) for r in results if r.outcome == "loss") / max(losses, 1)

        return {
            "total_trades": total,
            "wins": wins,
            "losses": losses,
            "win_rate": round(win_rate, 2),
            "avg_win_pips": round(avg_win, 2),
            "avg_loss_pips": round(avg_loss, 2),
        }
