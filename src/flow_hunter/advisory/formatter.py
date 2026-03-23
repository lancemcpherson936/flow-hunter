from flow_hunter.schemas.advisory import Advisory
from flow_hunter.schemas.control_state import ControlState
from flow_hunter.schemas.regime_state import RegimeState


class AdvisoryFormatter:
    def format(self, regime: RegimeState, control: ControlState, confidence: float) -> Advisory:
        if regime.label == "unstable":
            return Advisory(
                pair=regime.pair,
                regime=regime.label,
                control_side=control.side,
                verdict="wait",
                confidence=0.20,
                reasons=["unstable spread/tape"],
            )

        if control.side == "neutral":
            return Advisory(
                pair=regime.pair,
                regime=regime.label,
                control_side=control.side,
                verdict="wait",
                confidence=0.25,
                reasons=["no clear tape control"],
            )

        verdict = "hunt_long" if control.side == "long" else "hunt_short"
        reasons = []
        reasons.extend(regime.notes[:1])
        reasons.extend(control.notes[:1])

        return Advisory(
            pair=regime.pair,
            regime=regime.label,
            control_side=control.side,
            verdict=verdict,
            confidence=confidence,
            reasons=reasons,
        )
