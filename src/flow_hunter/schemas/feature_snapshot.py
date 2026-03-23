from dataclasses import dataclass


@dataclass(slots=True)
class FeatureSnapshot:
    pair: str
    tick_count: int
    directional_imbalance: float
    quote_asymmetry: float
    tick_velocity: float
    spread_mean: float
    spread_std: float
    displacement_pips: float
    burst_strength: float
    efficiency: float
