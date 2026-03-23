from flow_hunter.ingest.csv_replay import CSVReplayReader
from flow_hunter.runner import FlowHunterRunner
from flow_hunter.replay.evaluator import ReplayEvaluator
from flow_hunter.replay.metrics import Metrics


def main() -> None:
    rows = CSVReplayReader("data/sample_ticks.csv").read()
    runner = FlowHunterRunner()
    evaluator = ReplayEvaluator()
    metrics = Metrics()

    for raw in rows:
        result = runner.on_raw_tick(raw)
        advisory = result["advisory"]
        print(advisory)

        price = raw["bid"]
        if advisory["verdict"] == "hunt_long":
            evaluator.on_signal(price, "long")
        elif advisory["verdict"] == "hunt_short":
            evaluator.on_signal(price, "short")

        evaluator.on_tick(price)

    report = metrics.compute(evaluator.results)
    print("\n=== PERFORMANCE ===")
    print(report)


if __name__ == "__main__":
    main()
