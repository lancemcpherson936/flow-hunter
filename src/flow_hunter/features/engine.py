from flow_hunter.features.burst_strength import BurstStrength
from flow_hunter.features.directional_imbalance import DirectionalImbalance
from flow_hunter.features.efficiency import Efficiency
from flow_hunter.features.quote_asymmetry import QuoteAsymmetry
from flow_hunter.features.spread_stats import SpreadStats
from flow_hunter.features.tick_velocity import TickVelocity
from flow_hunter.schemas.feature_snapshot import FeatureSnapshot
from flow_hunter.schemas.tick import Tick


class FeatureEngine:
    def __init__(self) -> None:
        self.directional_imbalance = DirectionalImbalance()
        self.quote_asymmetry = QuoteAsymmetry()
        self.tick_velocity = TickVelocity()
        self.spread_stats = SpreadStats()
        self.burst_strength = BurstStrength()
        self.efficiency = Efficiency()

    def compute(self, ticks: list[Tick]) -> FeatureSnapshot:
        pair = ticks[-1].pair if ticks else "UNKNOWN"
        spread_mean, spread_std = self.spread_stats.compute(ticks)

        if len(ticks) >= 2:
            m = 100.0 if "JPY" in pair else 10000.0
            displacement_pips = (ticks[-1].mid - ticks[0].mid) * m
        else:
            displacement_pips = 0.0

        return FeatureSnapshot(
            pair=pair,
            tick_count=len(ticks),
            directional_imbalance=self.directional_imbalance.compute(ticks),
            quote_asymmetry=self.quote_asymmetry.compute(ticks),
            tick_velocity=self.tick_velocity.compute(ticks),
            spread_mean=spread_mean,
            spread_std=spread_std,
            displacement_pips=displacement_pips,
            burst_strength=self.burst_strength.compute(ticks),
            efficiency=self.efficiency.compute(ticks),
        )
