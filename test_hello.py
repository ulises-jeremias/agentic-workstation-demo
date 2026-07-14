"""Tests for hello.py CLI."""

import subprocess
import sys

import pytest


def run_hello(*args: str) -> subprocess.CompletedProcess[str]:
    """Run hello.py with given arguments and return the result."""
    return subprocess.run(
        [sys.executable, "hello.py", *args],
        capture_output=True,
        text=True,
    )


def test_default_greeting() -> None:
    """Default output should be 'Hello, World!'."""
    result = run_hello()
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, World!"


def test_custom_name() -> None:
    """--name flag should customize the greeting target."""
    result = run_hello("--name", "Alice")
    assert result.returncode == 0
    assert "Hello, Alice!" in result.stdout


def test_custom_greeting() -> None:
    """--greeting flag should customize the greeting word."""
    result = run_hello("--name", "Bob", "--greeting", "Hi")
    assert result.returncode == 0
    assert "Hi, Bob!" in result.stdout


def test_empty_name_rejected() -> None:
    """Empty --name should cause an error."""
    result = run_hello("--name", "")
    assert result.returncode != 0


def test_empty_greeting_rejected() -> None:
    """Empty --greeting should cause an error."""
    result = run_hello("--greeting", "")
    assert result.returncode != 0
    assert "--greeting cannot be empty" in result.stderr


def test_help_output() -> None:
    """--help should show usage information."""
    result = run_hello("--help")
    assert result.returncode == 0
    assert "--name" in result.stdout
    assert "--greeting" in result.stdout
    assert "--help" in result.stdout
