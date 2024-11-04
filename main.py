import streamlit as st
import sys
import os
import json
import tempfile
from typing import Dict
from config.analysis_config import AnalysisConfig
from config.chart_config import ChartConfig
from analysis.stock_analyzer import StockAnalyzer
from analysis.timeframe_strategy import StandardTimeframeStrategy
from chart.chart_generator import ChartGenerator
from generator.prompt_generator import PromptGenerator
from gpt.gpt_communicator import GPTCommunicator

# Import necessary modules for Selenium WebDriver
from selenium.common.exceptions import (
    WebDriverException,
    TimeoutException,
    NoSuchElementException
)

import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # Configure logging level

def load_exchange_data(path: str) -> Dict:
    """
    Load exchange data from a JSON file.

    Args:
        path (str): Path to the JSON file.

    Returns:
        Dict: Parsed JSON data.

    Raises:
        SystemExit: If the file is not found or JSON decoding fails.
    """
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"The file '{path}' was not found.")
        st.stop()
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON from the file '{path}'. Please check its format.")
        st.stop()
    except Exception as e:
        st.error(f"An unexpected error occurred while loading exchange data: {e}")
        st.stop()

def main():
    """
    Main function to run the Streamlit app for stock analysis.
    """
    st.set_page_config(page_title="Stock Analysis App", layout="wide")
    st.title("📈 Stock Analysis App")

    # Sidebar for API Key Input (Streamlit Secrets)
    st.sidebar.header("🔑 OpenAI API Key")
    if "API_KEY" in st.secrets:
        api_key = st.secrets["API_KEY"]
    else:
        st.sidebar.warning("API not found in")
        api_key = None

    # Optionally, allow users to input their own API key if not using secrets
    st.sidebar.markdown("---")
    st.sidebar.subheader("Or Enter Your API Key")
    user_api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

    # Determine which API key to use
    if user_api_key:
        api_key = user_api_key

    if not api_key:
        st.warning("Please provide your OpenAI API Key to proceed.")
        st.stop()

    # Initialize GPT Communicator
    try:
        gpt_communicator = GPTCommunicator(api_key)
        logger.info("GPT Communicator initialized successfully.")
    except Exception as e:
        st.error(f"Failed to initialize GPT Communicator: {e}")
        logger.error(f"Failed to initialize GPT Communicator: {e}")
        st.stop()

    # Load exchange data
    exchange_data = load_exchange_data("exchange_info.json")
    logger.info("Exchange data loaded successfully.")

    # Stock Symbol Entry
    symbol = st.text_input("📌 Enter Stock Symbol:", value="", max_chars=10).upper()
    if not symbol:
        st.info("Please enter a stock symbol to analyze (e.g., AAPL, TSLA).")
        st.stop()

    # Timeframe Selection
    timeframes = ['1m', '5m', '15m', '30m', '1h', '2h', '4h', '1d', '1W', '1M']
    timeframe_label = st.selectbox("⏰ Select Timeframe:", timeframes)
    logger.info(f"Selected timeframe: {timeframe_label}")

    # Prompt Type Selection with Summaries
    prompt_summaries = {
        '1': "Analysis with Image: Prepare for a trade by analyzing price and volume with technical indicators.",
        '2': "Profitable Analysis Strategy: Identify buying/selling opportunities using technical indicators.",
        '3': "Price Analysis: Use ICT trading methods to analyze prices and suggest a Call or Put position.",
        '4': "Market Structure Analysis: Examine key market structure elements like trends and breakout points.",
        '5': "Detailed Price and Image Analysis: Analyze price action and suggest trades with entry, take-profit, and stop-loss."
    }

    # Create a list of options with summaries
    prompt_options = [f"{key}: {summary}" for key, summary in prompt_summaries.items()]

    # Prompt Type Selection
    prompt_selection = st.selectbox("📝 Choose Prompt Type:", prompt_options)
    prompt_choice = prompt_selection.split(":")[0]
    logger.info(f"Selected prompt type: {prompt_choice}")

    # Analyze Button
    if st.button("🚀 Analyze"):
        with st.spinner("Analyzing..."):
            screenshot_path = None  # Initialize before try
            driver = None  # Initialize driver before try
            try:
                # Initialize analysis components
                timeframe_strategy = StandardTimeframeStrategy(timeframe_label)
                analyzer = StockAnalyzer(timeframe_strategy)
                chart_generator = ChartGenerator(ChartConfig())

                # Get analysis with indicators
                indicators = analyzer.get_analysis(symbol, exchange_data.get(symbol))
                logger.info(f"Analysis with indicators obtained for symbol: {symbol}")

                # Generate chart HTML content
                html_content = chart_generator.generate_html(
                    symbol,
                    exchange_data.get(symbol),
                    timeframe_strategy.get_tradingview_interval()
                )
                logger.info("Chart HTML content generated.")

                # Define output screenshot path
                with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp_screenshot:
                    screenshot_path = tmp_screenshot.name

                # Capture screenshot
                chart_generator.capture_screenshot(html_content, screenshot_path)
                logger.info(f"Screenshot captured at {screenshot_path}")

                # Display the chart image
                if os.path.exists(screenshot_path):
                    st.image(screenshot_path, caption=f"{symbol} Chart", use_column_width=True)
                    logger.info("Chart image displayed successfully.")
                else:
                    st.error("Failed to capture the chart screenshot.")
                    logger.error("Screenshot file does not exist.")

                # Initialize PromptGenerator with indicators
                prompt_gen = PromptGenerator(timeframe_label, indicators)
                logger.info("PromptGenerator initialized with indicators.")

                # Generate the prompt
                prompt = prompt_gen.generate_prompt(prompt_choice)
                logger.info(f"Prompt generated: {prompt}")

                if prompt != "Invalid choice":
                    response = gpt_communicator.send_analysis(prompt, screenshot_path)
                    st.success("🧠 GPT Analysis Completed!")
                    st.text_area("GPT Analysis Response:", value=response, height=300)
                    logger.info("GPT analysis completed and response displayed.")
                else:
                    st.error("Invalid prompt choice.")
                    logger.error("Invalid prompt choice selected.")
            except WebDriverException as wd_e:
                st.error(f"Selenium WebDriver error: {wd_e}")
                logger.error(f"Selenium WebDriver error: {wd_e}")
            except TimeoutException as te:
                st.error(f"Timeout error: {te}")
                logger.error(f"Timeout error: {te}")
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
                logger.error(f"An unexpected error occurred during analysis: {e}")
            finally:
                # Cleanup Selenium WebDriver is handled within ChartGenerator.capture_screenshot

                # Delete temporary screenshot if it exists
                if screenshot_path and os.path.exists(screenshot_path):
                    try:
                        os.remove(screenshot_path)
                        logger.info(f"Temporary screenshot {screenshot_path} deleted successfully.")
                    except Exception as remove_error:
                        st.warning(f"Failed to delete temporary screenshot: {remove_error}")
                        logger.warning(f"Failed to delete temporary screenshot: {remove_error}")

if __name__ == "__main__":
    main()
