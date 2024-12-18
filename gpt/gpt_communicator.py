from typing import Optional  # Add this line
import requests
import base64
import logging

logger = logging.getLogger(__name__)

class GPTCommunicator:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.openai.com/v1/chat/completions"

    def send_analysis(self, prompt: str, image_path: Optional[str] = None) -> str:
        base64_image = None
        if image_path:
            with open(image_path, "rb") as img_file:
                base64_image = base64.b64encode(img_file.read()).decode("utf-8")

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": "gpt-4o",
            "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}],
            "max_tokens": 3000
        }
        if base64_image:
            payload["messages"][0]["content"].append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}})

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except (requests.exceptions.RequestException, KeyError, IndexError) as e:
            logger.error(f"Error sending request to GPT API: {e}")
            return None
