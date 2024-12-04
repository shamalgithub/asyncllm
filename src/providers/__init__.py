from .openai_provider import OpenAIProvider
from .anthropic_provider import ClaudeProvider
from .google_provider import GoogleProvider
import sys
import asyncio

def get_supported_providers():
    supported_providers = ['openai' , 'claude', 'gemini']
    return f"The following LLM providers are supported \n {supported_providers}"

def get_provider(provider_name: str, api_key: str):

    if provider_name.lower() == "openai":
        return OpenAIProvider(api_key=api_key)
    elif provider_name.lower() == "claude":
        return ClaudeProvider(api_key=api_key)
    elif provider_name.lower() == "google":
        return GoogleProvider(api_key=api_key)
    else:
        raise ValueError(f"Unknown provider: {provider_name}. \nSupported Providers : {get_supported_providers()}")

#Windows has a issue when running asyncio code - to mitigate this use the following !!
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
