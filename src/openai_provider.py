"""Optional OpenAI provider implementation for Lab 02."""

from __future__ import annotations

from openai import OpenAI, OpenAIError

from src.models import LLMResponse
from src.provider import BaseProvider, ProviderError


class OpenAIProvider(BaseProvider):
    """Provider implementation backed by the OpenAI Python SDK."""

    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response using the OpenAI SDK."""
        # TODO: implement this method.
        try:
            client = OpenAI(api_key=self.api_key)
            completion = client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
            )
        except OpenAIError as exc:
            raise ProviderError(f"OpenAI request failed ({type(exc).__name__}).") from exc

        text = completion.choices[0].message.content
        if not text:
            raise ProviderError("OpenAI returned an empty response.")

        return LLMResponse(text=text, provider="openai", model=self.model)
