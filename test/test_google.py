from src.providers import get_provider
import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.mark.asyncio
async def test_google_chat_completion():
    messages = [
        {"role": "user", "content": "What's the capital of France?"}
    ]
    provider = get_provider("google", api_key=os.getenv("GOOGLE_API_KEY"))
    result = await provider.chat_completion(messages=messages)
    print(result)
    assert isinstance(result, dict)
