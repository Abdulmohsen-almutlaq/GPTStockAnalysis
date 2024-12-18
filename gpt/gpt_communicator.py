from typing import Optional
import base64
import logging
import openai

logger = logging.getLogger(__name__)

class GPTCommunicator:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def send_analysis(self, prompt: str, image_path: Optional[str] = None) -> str:
        base64_image = None
        if image_path:
            with open(image_path, "rb") as img_file:
                base64_image = base64.b64encode(img_file.read()).decode("utf-8")

        # Construct message content
        message_content = [{"type": "text", "text": prompt}]
        if base64_image:
            # Add the image content
            message_content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{base64_image}"}
            })

        try:
            # Send request using OpenAI SDK
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "user",
                        "content": message_content
                    }
                ],
                max_tokens=3000
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            logger.error(f"Error sending request to GPT API: {e}")
            return None
