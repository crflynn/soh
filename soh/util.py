"""Utility functions and decorators."""
from functools import wraps

import click
import pyperclip


def output(func):
    @wraps(func)
    def handle_output(*args, **kwargs):
        value = func(*args, **kwargs)
        clip = kwargs.get("clip", False)
        if clip:
            click.secho(value, fg="yellow", nl=False)
            click.secho(" (copied to clipboard 📋)", fg="green")
            pyperclip.copy(value)
        else:
            click.secho(value)

    return handle_output
