"""Behave environment hooks for browser setup and teardown.

This module keeps the project-level hook entrypoint thin and delegates behavior to
shared hooks under the hooks package.
"""
from __future__ import annotations

from hooks.behave_hooks import after_all, after_scenario, before_all, before_scenario

__all__ = ["before_all", "before_scenario", "after_scenario", "after_all"]
