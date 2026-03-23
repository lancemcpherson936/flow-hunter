from flow_hunter.schemas.control_state import ControlState
from flow_hunter.schemas.feature_snapshot import FeatureSnapshot


class DirectionalControl:
    def classify(self, features: FeatureSnapshot) -> ControlState:
        notes: list[str] = []

        strength = min(
            1.0,
            abs(features.directional_imbalance) * 0.5
            + abs(features.quote_asymmetry) * 0.2
            + abs(features.displacement_pips) * 0.05
            + features.burst_strength * 0.15
            + features.efficiency * 0.10,
        )

        if features.directional_imbalance > 0.25 and features.quote_asymmetry >= -0.10:
            notes.append("buyers control the tape")
            return ControlState(features.pair, "long", strength, notes)

        if features.directional_imbalance < -0.25 and features.quote_asymmetry <= 0.10:
            notes.append("sellers control the tape")
            return ControlState(features.pair, "short", strength, notes)

        notes.append("no clear control")
        return ControlState(features.pair, "neutral", 0.25, notes)
