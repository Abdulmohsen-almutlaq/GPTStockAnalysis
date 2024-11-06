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
            '5': "Detailed Price and Image Analysis: Analyze price action and suggest trades with entry, take-profit, and stop-loss.",
            '6':"Head and Shoulders, Double Top/Bottom, Triangles, Flags, Pennants, Wedges, Channels, Cup and Handle,"
        }
        print("\nSelect a Prompt Type:")
        for key, summary in summaries.items():
            print(f"{key}: {summary}")
    def generate_prompt(self, choice: str) -> str:
        """Generates a prompt based on the specified choice."""

        indicators_text = "\n".join([f"- **{key}:** {value}" for key, value in self.indicators.items()])

        prompts = {
            '1': f"""**Advanced Image and Market Analysis:**
        You are an elite day trader with decades of experience and a deep understanding of market psychology and advanced technical analysis. Your objective is to perform a comprehensive analysis of the market based on the following inputs:
        - **Timeframe:** {self.timeframe_label}
        - **Indicators and Readings:** {self.indicators}

        **Instructions:**
        1. **Deep Analysis:**
           - Examine the provided image meticulously to validate the accuracy of the indications.
           - Utilize advanced ICT (Inner Circle Trader) trading strategies to dissect candlestick patterns, including concepts like Smart Money Concepts (SMC), Market Maker Models (MMM), and Wyckoff Schematics.
           - Consider macroeconomic factors, market sentiment, and recent news that could impact the asset within the given timeframe.
        2. **Strategic Recommendation:**
           - Decide on a **Put** or **Call** position based on a synthesis of your technical and fundamental analysis.
           - Provide a **confidence level percentage**, explaining the rationale behind it with reference to specific data points.
           - Specify the optimal **contract type** (e.g., options, futures) and **expiration date**, justifying your choices in terms of risk management and potential ROI.
        3. **Example Analysis:**
           - *Detailed analysis of Moving Averages, RSI divergences, Stochastic Oscillator crossovers, Fibonacci retracement levels, etc.*
           - **Decision:** Call option
           - **Confidence Level:** 85% (due to bullish divergence on RSI and strong support at Fibonacci 61.8% level)
           - **Contract Expiration:** 2 weeks (aligning with expected time for pattern completion)
        """,

            '2': f"""**Comprehensive Profitable Analysis Strategy:**
        Act as a veteran day trader with expertise in exploiting market inefficiencies. Your objective is to analyze price action, volume, and intricate candlestick patterns for {self.timeframe_label} and {self.indicators}.
        - Integrate advanced technical indicators with historical data to identify high-probability buying or selling opportunities.
        - Consider patterns such as Elliott Waves, Harmonic Patterns (e.g., Gartley, Butterfly), and Ichimoku Clouds.
        - Provide a concise yet thorough summary, including entry and exit price recommendations, risk-reward ratios, and potential market catalysts.

        """,

            '3': f"""**In-Depth Price Analysis with ICT Methodologies:**
        As a seasoned day trader specializing in ICT strategies, analyze {self.indicators} and {self.timeframe_label} with a focus on the following:
        - Delve into ICT concepts such as liquidity pools, order blocks, fair value gaps, and imbalance zones.
        - Assess market maker manipulation patterns and identify potential stop hunts.
        - Provide a recommendation for a **Call** or **Put** position, supported by detailed confidence levels, precise entry and exit prices, and the underlying rationale.

        """,

            '4': f"""**Advanced Market Structure and Forecasting Analysis:**
        Perform a comprehensive analysis of the price action over the specified timeframe, focusing on key market structure elements:
        1. **Trend Analysis:**
           - Determine the primary and secondary trends (uptrend, downtrend, consolidation) using multi-timeframe analysis.
        2. **Critical Support and Resistance Levels:**
           - Identify and validate significant horizontal levels, trendlines, and pivot points.
           - Analyze volume at price (Volume Profile) to detect high-interest price zones.
        3. **Potential Breakout and Reversal Points:**
           - Use {self.indicators} to forecast breakout probabilities, including Bollinger Bands, Keltner Channels, and Average True Range (ATR).
           - Evaluate the impact of impending economic events or earnings reports.
        4. **Predictive Modeling:**
           - Apply statistical models or machine learning insights to anticipate future price movements.

        """,

            '5': f"""**Detailed Technical and Image Analysis with Precision Pricing:**
        You are a highly experienced day trader about to make a significant trade. Your objective is to analyze price action and volume meticulously based on the following inputs:
        - **Timeframe:** {self.timeframe_label}
        - **Indicators and Readings:** {self.indicators}

        **Instructions:**
        1. **Comprehensive Analysis:**
           - Employ a combination of technical indicators (e.g., MACD, ADX, Parabolic SAR) and chart patterns (e.g., Head and Shoulders, Double Tops/Bottoms).
           - Scrutinize the provided image to confirm indicator readings and uncover any hidden patterns or anomalies.
        2. **Strategic Recommendation:**
           - Decide between a **Put** or **Call** position, providing clear justification for your choice.
        3. **Precise Pricing Strategy:**
           - Calculate and provide exact figures for entry, take-profit, and stop-loss levels, ensuring they align with key support/resistance levels and risk management principles.
           - Present the prices in the exact format below:
             ```
             - ENTRY = [exact price]
             - TAKE-PROFIT = [exact price]
             - STOP-LOSS = [exact price]
             ```
        **Example Response:**
        - *After thorough analysis, including the identification of a bullish pennant formation and increasing volume, the following is recommended:*
        - **Decision:** Call option
        - **Pricing:**
        -ENTRY = $150.00
        -TAKE-PROFIT = $160.00
        -STOP-LOSS = $147.50
        """,
            '6':f"""- **Timeframe:** {self.timeframe_label}
        - **Indicators and Readings:** {self.indicators}
            Please conduct an in-depth analysis of the attached financial chart image to identify any common technical chart patterns present. Your analysis should include, but is not limited to, the following:

Pattern Identification:

Identify all recognizable technical chart patterns (e.g., Head and Shoulders, Double Top/Bottom, Triangles, Flags, Pennants, Wedges, Channels, Cup and Handle, etc.).
Specify the exact location of each pattern on the chart, including the relevant time frames and price levels.
Detailed Description:

Provide a thorough explanation of each identified pattern, detailing its formation process and key characteristics.
Explain the significance of trendlines, support and resistance levels, and how they relate to the pattern.
Volume Analysis:

Analyze the trading volume corresponding with each pattern.
Discuss how volume trends support or contradict the identified patterns.
Technical Indicators:

Incorporate other technical indicators present on the chart (e.g., Moving Averages, RSI, MACD, Bollinger Bands).
Explain how these indicators confirm or challenge the validity of the identified patterns.
Implications for Future Price Movements:

Assess the potential bullish or bearish implications of each pattern.
Provide historical context or statistical data regarding the reliability of each pattern in forecasting future price movements.
Trading Strategies:

Suggest potential trading strategies based on the identified patterns, including optimal entry and exit points.
Include recommendations for stop-loss and take-profit levels.
Discuss risk management considerations associated with these strategies.
Multiple Time Frame Analysis:

If applicable, analyze the chart across different time frames (e.g., daily, weekly, monthly).
Explain how patterns in different time frames may interact or influence overall market sentiment.
Confidence Levels and Alternative Scenarios:

Assign a confidence level to each identified pattern based on its clarity and supporting evidence.
Mention any alternative interpretations or conflicting signals that could affect the analysis.
Discuss how market conditions or external factors might influence the effectiveness of the patterns.
Conclusion:

Summarize the key findings of your analysis.
Provide a reasoned outlook on potential future price movements based on the combined evidence from patterns and indicators.
Please ensure that your analysis is comprehensive, precise, and utilizes advanced technical analysis techniques. Use professional language appropriate for a financial analyst's report, and strive to provide the most accurate interpretation possible.""",
            '7': f"""**Advanced Image and Market Analysis:**
        You are an elite day trader with decades of experience and a deep understanding of market psychology and advanced technical analysis. Your objective is to perform a comprehensive analysis of the market based on the following inputs:
        - **Timeframe:** {self.timeframe_label}
        - **Indicators and Readings:** {self.indicators}
        the profit but be above 7% also if its bad time to go say it to me 
        
        **Instructions:**
        1. **Deep Analysis:**
           - Examine the provided image meticulously to validate the accuracy of the indications.
           - Utilize advanced ICT (Inner Circle Trader) trading strategies to dissect candlestick patterns, including concepts like Smart Money Concepts (SMC), Market Maker Models (MMM), and Wyckoff Schematics.
           - Consider macroeconomic factors, market sentiment, and recent news that could impact the asset within the given timeframe.
        2. **Strategic Recommendation:**
           - Decide on a **Put** or **Call** position based on a synthesis of your technical and fundamental analysis.
           - Provide a **confidence level percentage**, explaining the rationale behind it with reference to specific data points.
           - Specify the optimal **contract type** (e.g., options, futures) and **expiration date**, justifying your choices in terms of risk management and potential ROI.
        3. **Example Analysis:**
           - *Detailed analysis of Moving Averages, RSI divergences, Stochastic Oscillator crossovers, Fibonacci retracement levels, etc.*
           - **Decision:** Call option
           - **Confidence Level:** 85% (due to bullish divergence on RSI and strong support at Fibonacci 61.8% level)
           - **Contract Expiration:** 2 weeks (aligning with expected time for pattern completion)
        """
}
        return prompts.get(choice, "Invalid choice")
