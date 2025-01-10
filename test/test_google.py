from async_llm.providers import get_provider
import os
from dotenv import load_dotenv
import pytest

load_dotenv()

@pytest.mark.asyncio
async def test_google_chat_completion():
    model = "gemini-2.0-flash-exp"
    messages = [
        {"role": "user", "content": "What's the capital of France?"}
    ]
    provider = get_provider("google", api_key=os.getenv("GOOGLE_API_KEY"))
    result = await provider.chat_completion(model=model, messages=messages)
    print(result)
    assert isinstance(result, dict)
