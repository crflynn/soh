"""Utility functions and decorators."""
from functools import wraps

import click
import pyperclip


def clipboard_output(func):
    @click.option("-c", "--clip", is_flag=True, help="copy to clipboard")
    @wraps(func)
    def handle_output(*args, **kwargs):
        clip = kwargs.pop("clip", False)
        value = func(*args, **kwargs)
        if clip:
            click.secho(value, fg="yellow", nl=False)
            click.secho(" (copied to clipboard 📋)", fg="green")
            pyperclip.copy(value)
        else:
            click.secho(value)

    return handle_output
