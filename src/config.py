"""Student-facing configuration helpers for Lab 02."""

from __future__ import annotations

import os


class ConfigurationError(ValueError):
    """Raised when a required setting is missing or a setting is invalid."""


def load_config() -> dict:
    """
    Load configuration from environment variables.

    Expected keys:
    - LLM_PROVIDER
    - OPENAI_API_KEY
    - OPENAI_MODEL
    """
    # TODO: implement this function.
    return {
        "LLM_PROVIDER": os.getenv("LLM_PROVIDER", "mock"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
        "OPENAI_MODEL": os.getenv("OPENAI_MODEL", ""),
    }
