from dataclasses import dataclass
from typing import Dict

@dataclass
class AnalysisConfig:
    symbol: str
    exchange: str
    timeframe: str
    indicators: Dict
