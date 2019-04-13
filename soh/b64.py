"""Base64 CLI functionality.

Entry point: $ soh b64d [OPTS] <text>
Entry point: $ soh b64e [OPTS] <text>
"""
import base64

import click
import pyperclip


@click.command(short_help="Decode base64 strings")
@click.argument("text")
@click.option("-c", "--clip", is_flag=True, help="copy to clipboard")
def b64decode(text, clip):
    """Decode base64."""
    value = base64.b64decode(text.encode("utf-8")).decode("utf-8")
    if clip:
        click.secho(value, fg="yellow")
        pyperclip.copy(value)
    else:
        click.secho(value)


@click.command(short_help="Encode strings to base64")
@click.argument("text")
@click.option("-c", "--clip", is_flag=True, help="copy to clipboard")
def b64encode(text, clip):
    """Encode base64."""
    value = base64.b64encode(text.encode("utf-8")).decode("utf-8")
    if clip:
        click.secho(value, fg="yellow")
        pyperclip.copy(value)
    else:
        click.secho(value)
