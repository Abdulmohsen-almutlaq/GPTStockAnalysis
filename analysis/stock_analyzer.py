from tradingview_ta import TA_Handler
from typing import Dict
import logging

logger = logging.getLogger(__name__)

class StockAnalyzer:
    def __init__(self, timeframe_strategy):
        self.timeframe_strategy = timeframe_strategy

    def get_analysis(self, symbol: str, exchange: str) -> Dict:
        handler = TA_Handler(
            symbol=symbol,
            screener="america",
            exchange=exchange,
            interval=self.timeframe_strategy.get_analysis_interval()
        )
        try:
            analysis = handler.get_analysis()
            return analysis.indicators
        except Exception as e:
            logger.error(f"Error fetching analysis: {e}")
            raise
