from dataclasses import dataclass, field


@dataclass(slots=True)
class RegimeState:
    pair: str
    label: str
    score: float
    notes: list[str] = field(default_factory=list)
