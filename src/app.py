"""Student-facing application logic for Lab 02."""

from __future__ import annotations

from src.config import ConfigurationError, load_config
from src.mock_provider import MockProvider
from src.openai_provider import OpenAIProvider
from src.provider import ProviderError

MAX_PROMPT_LENGTH = 4000


def validate_prompt(prompt: str) -> str:
    """Validate and normalize a user prompt."""
    # TODO: implement this function.
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    cleaned = prompt.strip()
    if not cleaned:
        raise ValueError("Prompt must not be empty or whitespace only.")
    if len(cleaned) > MAX_PROMPT_LENGTH:
        raise ValueError(f"Prompt must be at most {MAX_PROMPT_LENGTH} characters.")
    return cleaned


def create_provider(config: dict):
    """Select and instantiate the configured provider."""
    # TODO: implement this function.
    provider_name = config.get("LLM_PROVIDER", "mock")

    if provider_name == "mock":
        return MockProvider()

    if provider_name == "openai":
        if not config.get("OPENAI_API_KEY"):
            raise ConfigurationError("OPENAI_API_KEY must be set when LLM_PROVIDER=openai.")
        if not config.get("OPENAI_MODEL"):
            raise ConfigurationError("OPENAI_MODEL must be set when LLM_PROVIDER=openai.")
        return OpenAIProvider(api_key=config["OPENAI_API_KEY"], model=config["OPENAI_MODEL"])

    raise ConfigurationError("Unsupported LLM_PROVIDER. Supported values: mock, openai.")


def generate_response(prompt: str) -> dict:
    """Generate a normalized response for a user prompt."""
    # TODO: implement this function.
    clean_prompt = validate_prompt(prompt)
    provider = create_provider(load_config())

    try:
        response = provider.generate(clean_prompt)
    except ProviderError:
        raise
    except Exception as exc:
        raise ProviderError("The LLM provider failed to generate a response.") from exc

    return {"text": response.text, "provider": response.provider, "model": response.model}


def main() -> None:
    """Simplified CLI entry point for the lab."""
    print("LLMOps Lab 02")

    try:
        config = load_config()
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("Provider:", config.get("LLM_PROVIDER", "mock"))

    prompt = input("\nEnter prompt:\n> ")

    try:
        response = generate_response(prompt)
    except NotImplementedError:
        print("Complete the TODO implementations in src/config.py, src/provider.py, src/mock_provider.py, src/openai_provider.py, and src/app.py before running this demo.")
        return

    print("\nResponse:")
    print(response["text"])


if __name__ == "__main__":
    main()
