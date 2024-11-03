from typing import Dict
class PromptGenerator:
    def __init__(self, timeframe_label: str, indicators: Dict):
        self.timeframe_label = timeframe_label
        self.indicators = indicators
    def display_prompt_summaries(self):
        """Displays a summary for each prompt type."""
        summaries = {
            '1': "Analysis with Image: Prepare for a trade by analyzing price and volume with technical indicators.",
            '2': "Profitable Analysis Strategy: Identify buying/selling opportunities using technical indicators.",
            '3': "Price Analysis: Use ICT trading methods to analyze prices and suggest a Call or Put position.",
            '4': "Market Structure Analysis: Examine key market structure elements like trends and breakout points.",
            '5': "Detailed Price and Image Analysis: Analyze price action and suggest trades with entry, take-profit, and stop-loss."
        }
        print("\nSelect a Prompt Type:")
        for key, summary in summaries.items():
            print(f"{key}: {summary}")
    def generate_prompt(self, choice: str) -> str:
        """Generates a prompt based on the specified choice."""

        indicators_text = "\n".join([f"- **{key}:** {value}" for key, value in self.indicators.items()])

        prompts = {
            '1': f"""Analysis with Image: You are an experienced day trader preparing to enter a trade. 
        Objective is to analyze the price and volume based on the following inputs:
        - **Timeframe:** {self.timeframe_label}
        - **Readings:** {self.indicators}

        **Instructions:**
        1. **Analysis:**
           - Analyze the image to determine if indications are accurate.
           - Analyze candlestick patterns using the ICT trading strategy.
        2. **Recommendation:**
           - Suggest a **Put** or **Call** position based on your analysis.
           - Provide a confidence level percentage.
           - Specify contract type and expiration date.
           
           
        3. **Example Analysis:**
            think twice before makeing decision
           - Moving Averages, RSI, Stochastic Oscillator, etc. analysis...
           - **Decision:** Call option
           - **Confidence Level:** any prcentage that you think is right also think twice before makeing decision
           - **Contract Expiration:** 1-2 weeks
                    """,

            '2': f"""Profitable Analysis Strategy:
        Act as an experienced day trader. Objective is to analyze price, volume, and candlestick patterns for {self.timeframe_label} and {self.indicators}. 
        - Focus on identifying buying or selling opportunities based on technical indicators and historical data.
        - Provide a short summary and recommended prices.
                    """,

            '3': f"""Price Analysis:
        As a day trader using ICT methodologies, analyze {self.indicators} and {self.timeframe_label}.
        - Focus on ICT concepts like liquidity pools, order blocks, fair value gaps.
        - Suggest **Call** or **Put** based on confidence and prices.
                    """,

            '4': f"""Market Structure Analysis:
        Analyze price action over the given timeframe and identify key market structure elements:
        1. Trend identification (uptrend, downtrend, consolidation).
        2. Support and resistance levels.
        3. Potential breakout points, using {self.indicators}.
                    """,

            '5': f"""Detailed Price and Image Analysis:
        You are an experienced day trader preparing to enter a trade. Objective is to analyze price and volume based on inputs:
        - **Timeframe:** {self.timeframe_label}
        - **Readings:** {self.indicators}
        **Instructions:**
        1. **Analysis:**
           - Use technical indicators.
           - Analyze the image for accuracy.
        2. **Recommendation:**
           - Suggest a **Put** or **Call** position.
        3. **Pricing:**
           - Provide entry, take-profit, and stop-loss prices in the exact format below:
             ```
             - ENTRY =
             - TAKE-PROFIT =
             - STOPLOSS =
             ```
        Example Response:
        Only summary, prices, and recommendation.
                    """
        }
        return prompts.get(choice, "Invalid choice")
