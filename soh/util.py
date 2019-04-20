"""Utility functions and decorators."""
from functools import wraps

import click
import pyperclip
import requests


COPIED_TO_CLIPBOARD_MESSAGE = " (copied to clipboard 📋)"


def clipboard_output(func):
    @click.option("-c", "--clip", is_flag=True, help="copy to clipboard")
    @wraps(func)
    def handle_output(*args, **kwargs):
        clip = kwargs.pop("clip", False)
        protect = kwargs.pop("protect", False)
        value = func(*args, **kwargs)
        if clip:
            if value != "" and not protect:
                click.secho(value, fg="yellow", nl=False)
            click.secho(COPIED_TO_CLIPBOARD_MESSAGE, fg="green")
            pyperclip.copy(value)
        else:
            if value != "" and not protect:
                click.secho(value)

    return handle_output


def ensure_ok_response(response, message):
    try:
        response.raise_for_status()
    except requests.RequestException:
        raise click.ClickException(message)
