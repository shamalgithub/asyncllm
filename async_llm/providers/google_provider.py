from async_llm.providers.abstract_basellm import BaseLLMProvider
import httpx
from typing import List, Dict
from urllib.parse import urljoin, urlencode

class GoogleProvider(BaseLLMProvider):
    def __init__(self, api_key: str) -> None:
        super().__init__()
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
        }

    def _create_base_url(self, model:str="gemini-1.5-flash"):
        base_url = "https://generativelanguage.googleapis.com/v1beta/"
        endpoint = f"models/{model}:generateContent"
        query_params = {"key": self.api_key}
        base_url = urljoin(base_url, endpoint) + "?" + urlencode(query_params)
        return base_url

    async def chat_completion(self, model:str, messages: List[Dict[str, str]]):
        self.model = model
        url = self._create_base_url(model)
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


