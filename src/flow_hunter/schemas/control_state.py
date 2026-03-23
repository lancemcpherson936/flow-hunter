from dataclasses import dataclass, field


@dataclass(slots=True)
class ControlState:
    pair: str
    side: str
    strength: float
    notes: list[str] = field(default_factory=list)
