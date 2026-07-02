"""Compatibility wrapper for Behave hooks.

Behave will discover this file when running from the features directory. It simply
re-exports the shared hook implementation from the hooks package.
"""
from __future__ import annotations

from hooks.behave_hooks import after_all, after_scenario, before_all, before_scenario

__all__ = ["before_all", "before_scenario", "after_scenario", "after_all"]
