from dataclasses import dataclass

@dataclass
class ChartConfig:
    width: int = 1560
    height: int = 900
    theme: str = "light"
    style: str = "1"
    locale: str = "en"
    toolbar_bg: str = "#f1f3f6"
    enable_publishing: bool = False
    allow_symbol_change: bool = True
