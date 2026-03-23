from dataclasses import dataclass, field


@dataclass(slots=True)
class Advisory:
    pair: str
    regime: str
    control_side: str
    verdict: str
    confidence: float
    reasons: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "pair": self.pair,
            "regime": self.regime,
            "control_side": self.control_side,
            "verdict": self.verdict,
            "confidence": self.confidence,
            "reasons": self.reasons,
        }
