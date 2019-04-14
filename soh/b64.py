"""Base64 CLI functionality.

Entry point: $ soh b64d [OPTS] <text>
Entry point: $ soh b64e [OPTS] <text>
"""
import base64

import click

from soh.util import clipboard_output


@click.group(invoke_without_command=False, short_help="Base64 operations")
def b64():
    pass


@b64.command(short_help="Decode base64 strings")
@click.argument("text")
@clipboard_output
def d(text):
    """Decode base64."""
    return base64.b64decode(text.encode("utf-8")).decode("utf-8")


@b64.command(short_help="Encode strings to base64")
@click.argument("text")
@clipboard_output
def e(text):
    """Encode base64."""
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")
