# 📈 GPTStockAnalysis

![App Screenshot](https://github.com/Abdulmohsen-almutlaq/GPTStockAnalysis/blob/main/assets/screenshot_1.png)

## 📊 About This App

**GPTStockAnalysis** is a web application that allows users to analyze stock performance, generate detailed charts, and receive insightful analyses powered by OpenAI's GPT. Whether you're an investor, trader, or just curious about stock trends, this app provides the tools you need to make informed decisions.

## 🔧 Features

- **Real-time Stock Analysis:** Get up-to-date information on your favorite stocks.
- **Custom Timeframes:** Choose from various timeframes to suit your analysis needs.
- **Automated Chart Generation:** Generate and capture screenshots of stock charts effortlessly.
- **GPT-Powered Insights:** Receive detailed analyses and recommendations based on your selected parameters.

## 🛠️ Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Abdulmohsen-almutlaq/GPTStockAnalysis.git
    cd GPTStockAnalysis
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install System Dependencies**

    Create a `packages.txt` file in the root directory with the following content:

    ```plaintext
    chromium
    chromium-driver
    ```

    This ensures that Chromium and its driver are installed, which are necessary for Selenium.

    **Note:** If you're deploying to **Streamlit Cloud**, ensure that this `packages.txt` file is included in your repository root. Streamlit Cloud will automatically install the specified system packages during deployment.

## 🔒 Configuration

### 1. OpenAI API Key

The app requires an OpenAI API key to generate GPT-powered insights. You can provide this key in two ways:

#### a. Using Streamlit Secrets

1. **Locally:** Create a `.streamlit/secrets.toml` file in the root directory:

    ```toml
    API_KEY = "your_openai_api_key_here"
    ```

2. **On Streamlit Cloud:**
   - Navigate to your app on Streamlit Cloud.
   - Go to the **"Settings"** tab.
   - Click on **"Secrets"** and add your `API_KEY` there.

#### b. User Input

If the API key isn't found in `secrets.toml`, users can manually enter their API key in the sidebar.

### 2. Exchange Data

Ensure that the `exchange_info.json` file is present in the root directory. This file contains necessary exchange information for stock symbols.

## 💡 Usage

1. **Run the App**

    ```bash
    streamlit run app.py
    ```

2. **Interact with the App**

    - **Enter Stock Symbol:** Input the ticker symbol of the stock you wish to analyze (e.g., AAPL, TSLA).
    - **Select Timeframe:** Choose the desired timeframe for your analysis.
    - **Choose Prompt Type:** Select the type of analysis prompt for GPT.
    - **Analyze:** Click the "🚀 Analyze" button to generate the chart and receive GPT-powered insights.

3. **View Results**

    - **Chart Image:** The app will display the generated stock chart.
    - **GPT Analysis:** View the detailed analysis and recommendations provided by GPT.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and create a pull request.

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📫 Contact

Abdulmohsen Almutlaq - [abdul.almutlaq@hotmail.com](mailto:abdul.almutlaq@hotmail.com)

Project Link: [https://github.com/Abdulmohsen-almutlaq/GPTStockAnalysis](https://github.com/Abdulmohsen-almutlaq/GPTStockAnalysis)
