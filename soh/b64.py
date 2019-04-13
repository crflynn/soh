"""Base64 CLI functionality.

Entry point: $ soh b64d [OPTS] <text>
Entry point: $ soh b64e [OPTS] <text>
"""
import base64

import click

from soh.util import clipboard_output


@click.command(short_help="Decode base64 strings")
@click.argument("text")
@clipboard_output
def b64decode(text):
    """Decode base64."""
    return base64.b64decode(text.encode("utf-8")).decode("utf-8")


@click.command(short_help="Encode strings to base64")
@click.argument("text")
@clipboard_output
def b64encode(text):
    """Encode base64."""
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")
