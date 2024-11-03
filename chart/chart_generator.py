from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    WebDriverException,
    TimeoutException,
    NoSuchElementException
)
import time
import logging
import tempfile
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # Configure logging level

class ChartGenerator:
    def __init__(self, config):
        self.config = config

    def generate_html(self, symbol: str, exchange: str, interval: str) -> str:
        """
        Generates the HTML content for the TradingView widget.

        Args:
            symbol (str): Stock symbol (e.g., AAPL).
            exchange (str): Exchange name (e.g., NASDAQ).
            interval (str): Timeframe interval (e.g., 1h).

        Returns:
            str: HTML content with TradingView widget.
        """
        html_content = f"""
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container">
          <div id="tradingview_chart"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget(
          {{
            "width": 1760,
            "height": 610,
            "symbol": "{exchange}:{symbol}",
            "interval": "{interval}",
            "timezone": "Etc/UTC",
            "theme": "light",
            "style": "1",
            "locale": "en",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "allow_symbol_change": true,
            "container_id": "tradingview_chart"
          }}
          );
          </script>
        </div>
        <!-- TradingView Widget END -->
        """
        return html_content

    def capture_screenshot(self, html_content: str, output_path: str) -> None:
        """
        Captures a screenshot of the TradingView chart.

        Args:
            html_content (str): HTML content to render.
            output_path (str): Path to save the screenshot.

        Raises:
            WebDriverException: If the WebDriver fails to initialize.
            TimeoutException: If the TradingView widget fails to load within the specified time.
            Exception: For any other unforeseen errors.
        """
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--hide-scrollbars")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--log-level=3")  # Suppress warnings

        # Create a temporary directory for HTML file
        with tempfile.TemporaryDirectory() as tmp_dir:
            temp_html_path = Path(tmp_dir) / "temp_chart.html"
            temp_html_path.write_text(html_content, encoding='utf-8')

            try:
                # Initialize WebDriver
                service = Service(ChromeDriverManager().install())
                driver = webdriver.Chrome(service=service, options=chrome_options)
                logger.info("WebDriver initialized successfully.")

                # Open the temporary HTML file
                driver.get(temp_html_path.as_uri())
                logger.info(f"Opened temporary HTML file at {temp_html_path.as_uri()}")

                # Wait until the TradingView widget is loaded
                try:
                    # Wait up to 30 seconds for the widget to load
                    WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.ID, "tradingview_chart"))
                    )
                    logger.info("TradingView widget loaded successfully.")
                except TimeoutException:
                    logger.error("TradingView widget failed to load within the timeout period.")
                    raise TimeoutException("TradingView widget failed to load within the timeout period.")

                # Additional wait to ensure the widget fully renders
                time.sleep(5)  # Adjust as necessary

                # Capture screenshot
                driver.save_screenshot(output_path)
                logger.info(f"Screenshot saved as {output_path}")

            except WebDriverException as wd_e:
                logger.error(f"Selenium WebDriver error: {wd_e}")
                raise WebDriverException(f"Selenium WebDriver error: {wd_e}")
            except TimeoutException as te:
                logger.error(f"Timeout error: {te}")
                raise TimeoutException(f"Timeout error: {te}")
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                raise e
            finally:
                # Ensure the driver is closed to free resources
                try:
                    driver.quit()
                    logger.info("WebDriver closed successfully.")
                except Exception as quit_error:
                    logger.warning(f"Failed to close WebDriver: {quit_error}")

        # No need to manually delete the HTML file as TemporaryDirectory handles it

