from src.providers.abstract_basellm import BaseLLMProvider
import httpx
from typing import List, Dict
import json
from urllib.parse import urljoin, urlencode

class GoogleProvider(BaseLLMProvider):
    def __init__(self, api_key: str) -> None:
        super().__init__()
        base_url = "https://generativelanguage.googleapis.com/v1beta/"
        endpoint = "models/gemini-1.5-flash:generateContent"
        query_params = {"key": api_key}

        self.base_url = urljoin(base_url, endpoint) + "?" + urlencode(query_params)
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
        }

    async def chat_completion(self, messages: List[Dict[str, str]]):
        url = self.base_url
        headers = self.headers
        data = {
            "contents": [
                {
                    "role": message["role"],
                    "parts": [{"text": message["content"]}]
                }
                for message in messages
            ]
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url=url, json=data, headers=headers)
                response.raise_for_status()
                return response.json()
        except httpx.RequestError as e:
            return f"ERROR {e}"

    async def stream_chat_completion(self):
        return None


