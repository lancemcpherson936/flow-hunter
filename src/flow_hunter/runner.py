from flow_hunter.advisory.formatter import AdvisoryFormatter
from flow_hunter.control.directional_control import DirectionalControl
from flow_hunter.features.engine import FeatureEngine
from flow_hunter.ingest.buffers import TickBuffer
from flow_hunter.ingest.tick_normalizer import TickNormalizer
from flow_hunter.regime.regime_classifier import RegimeClassifier


class FlowHunterRunner:
    def __init__(self, buffer_size: int = 200, analysis_window: int = 30) -> None:
        self.normalizer = TickNormalizer()
        self.buffer = TickBuffer(maxlen=buffer_size)
        self.features = FeatureEngine()
        self.regime = RegimeClassifier()
        self.control = DirectionalControl()
        self.formatter = AdvisoryFormatter()
        self.analysis_window = analysis_window

    def on_raw_tick(self, raw_tick: dict) -> dict:
        tick = self.normalizer.normalize(raw_tick)
        self.buffer.append(tick)

        ticks = self.buffer.last_n(self.analysis_window)
        features = self.features.compute(ticks)
        regime = self.regime.classify(features)
        control = self.control.classify(features)

        confidence = min(
            0.95,
            0.35 * regime.score
            + 0.45 * control.strength
            + 0.10 * features.burst_strength
            + 0.10 * features.efficiency,
        )

        advisory = self.formatter.format(regime, control, confidence)

        return {
            "tick": tick,
            "features": features,
            "regime": regime,
            "control": control,
            "advisory": advisory.to_dict(),
        }
