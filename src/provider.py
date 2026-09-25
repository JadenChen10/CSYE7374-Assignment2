"""Provider abstraction for Lab 02."""

from __future__ import annotations

from abc import ABC, abstractmethod

from src.models import LLMResponse


class ProviderError(RuntimeError):
    """Raised when an LLM provider fails to produce a response."""


class BaseProvider(ABC):
    """Abstract provider interface."""

    @abstractmethod
    def generate(self, prompt: str) -> LLMResponse:
        """Generate a response for the given prompt.

        Every provider must return an application-level ``LLMResponse``
        (never a raw SDK object) and raise ``ProviderError`` on provider-side
        failures, with a message that never includes secrets such as API keys.
        """
        # TODO: implement this abstract method contract.
        raise NotImplementedError("Concrete providers must implement generate().")
