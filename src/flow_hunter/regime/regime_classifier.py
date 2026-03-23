from flow_hunter.schemas.feature_snapshot import FeatureSnapshot
from flow_hunter.schemas.regime_state import RegimeState


class RegimeClassifier:
    def classify(self, features: FeatureSnapshot) -> RegimeState:
        notes: list[str] = []

        if features.tick_count < 5:
            return RegimeState(
                pair=features.pair,
                label="insufficient_data",
                score=0.0,
                notes=["not enough ticks"],
            )

        abs_imb = abs(features.directional_imbalance)
        abs_disp = abs(features.displacement_pips)

        if features.spread_mean >= 1.2 or features.spread_std >= 0.5:
            notes.append("spread is unstable")
            return RegimeState(features.pair, "unstable", 0.75, notes)

        if abs_disp < 0.5 and features.tick_velocity > 8 and features.spread_std < 0.15:
            notes.append("tight range with active flow")
            return RegimeState(features.pair, "compression", 0.72, notes)

        if abs_imb > 0.45 and abs_disp > 0.8 and features.efficiency > 0.45:
            notes.append("directional expansion detected")
            return RegimeState(features.pair, "expansion", 0.80, notes)

        notes.append("mixed tape behavior")
        return RegimeState(features.pair, "balanced", 0.55, notes)
