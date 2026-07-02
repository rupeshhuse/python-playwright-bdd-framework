"""Configuration loader for environment-specific settings.

The loader reads environment-specific .env files so the framework can switch
between QA, UAT, and PROD values without changing code.
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent
ENVIRONMENTS_DIR = PROJECT_ROOT / "config" / "environments"


class ConfigReader:
    """Load environment variables from the active environment file."""

    def __init__(self, environment: str | None = None) -> None:
        self.environment = environment or os.getenv("ENVIRONMENT", "qa")
        self.env_file = ENVIRONMENTS_DIR / f"{self.environment}.env"
        self._loaded_values: dict[str, str] = {}
        self._load()

    def _load(self) -> None:
        """Load .env values if the environment file exists."""
        if self.env_file.exists():
            load_dotenv(self.env_file, override=True)
            for key, value in os.environ.items():
                self._loaded_values[key] = value

    def get(self, key: str, default: Any | None = None) -> Any:
        """Read a configuration value from the environment with a safe fallback."""
        return self._loaded_values.get(key.upper(), os.getenv(key.upper(), default))

    def get_bool(self, key: str, default: bool = False) -> bool:
        """Parse boolean values from configuration."""
        value = self.get(key, default)
        if isinstance(value, bool):
            return value
        return str(value).strip().lower() in {"1", "true", "yes", "on"}

    def get_int(self, key: str, default: int = 0) -> int:
        """Parse integer values from configuration."""
        value = self.get(key, default)
        return int(value)
