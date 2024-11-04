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
        # Removed the popup warning
        api_key = None

    # Optionally, allow users to input their own API key if not using secrets
    st.sidebar.markdown("---")
    st.sidebar.subheader("Or Enter Your API Key")
    user_api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

    # Determine which API key to use
    if user_api_key:
        api_key = user_api_key

    if not api_key:
        st.warning("Please provide your OpenAI API Key to proceed. You can add it to the `.streamlit/secrets.toml` file or enter it in the sidebar.")
        st.stop()

    # Initialize GPT Communicator
    try:
        gpt_communicator = GPTCommunicator(api_key)
        logger.info("GPT Communicator initialized successfully.")
    except Exception as e:
        st.error(f"Failed to initialize GPT Communicator: {e}")
        logger.error(f"Failed to initialize GPT Communicator: {e}")
        st.stop()

    # ... rest of your code ...
