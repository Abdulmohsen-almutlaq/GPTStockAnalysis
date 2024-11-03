from abc import ABC, abstractmethod
from tradingview_ta import Interval

class TimeframeStrategy(ABC):
    @abstractmethod
    def get_tradingview_interval(self) -> str:
        pass

    @abstractmethod
    def get_analysis_interval(self) -> str:
        pass

class StandardTimeframeStrategy(TimeframeStrategy):
    def __init__(self, timeframe: str):
        self.timeframe = timeframe
        self._interval_mapping = {
            '1m': (Interval.INTERVAL_1_MINUTE, '1'),
            '5m': (Interval.INTERVAL_5_MINUTES, '5'),
            '15m': (Interval.INTERVAL_15_MINUTES, '15'),
            '30m': (Interval.INTERVAL_30_MINUTES, '30'),
            '1h': (Interval.INTERVAL_1_HOUR, '60'),
            '2h': (Interval.INTERVAL_2_HOURS, '120'),
            '4h': (Interval.INTERVAL_4_HOURS, '240'),
            '1d': (Interval.INTERVAL_1_DAY, 'D'),
            '1W': (Interval.INTERVAL_1_WEEK, 'W'),
            '1M': (Interval.INTERVAL_1_MONTH, 'M')
        }

    def get_tradingview_interval(self) -> str:
        if self.timeframe not in self._interval_mapping:
            raise ValueError(f"Invalid timeframe: {self.timeframe}")
        return self._interval_mapping[self.timeframe][1]

    def get_analysis_interval(self) -> str:
        if self.timeframe not in self._interval_mapping:
            raise ValueError(f"Invalid timeframe: {self.timeframe}")
        return self._interval_mapping[self.timeframe][0]
