"""Centralized configuration loaded from environment-specific .env files."""
import os
from pathlib import Path
from dotenv import load_dotenv


class Settings:
    def __init__(self, env: str = "qa") -> None:
        self.env = env
        env_file = Path(__file__).parent / f"{env}.env"
        if env_file.exists():
            load_dotenv(env_file, override=True)

        self.base_url: str = os.getenv("BASE_URL", "https://www.google.com")
        self.api_base_url: str = os.getenv("API_BASE_URL", "https://httpbin.org")
        self.username: str = os.getenv("USERNAME", "")
        self.password: str = os.getenv("PASSWORD", "")
        self.browser: str = os.getenv("BROWSER", "chromium")
        self.headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
        self.timeout: int = int(os.getenv("TIMEOUT", "30000"))


def get_settings(env: str = None) -> Settings:
    return Settings(env or os.getenv("TEST_ENV", "qa"))
