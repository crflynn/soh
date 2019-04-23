"""Base64 CLI functionality.

Entry point: $ soh b64d [OPTS] <text>
Entry point: $ soh b64e [OPTS] <text>
"""
import base64

import click

from soh.util import clipboard_output


# TODO consider checking clipboard if no input provided
# TODO consider applying missing padding and including a warning


@click.group(invoke_without_command=False, short_help="Base64 operations")
def b64():
    """Base64 decoding and encoding."""
    pass  # pragma: no cover


@b64.command(short_help="Decode base64 strings")
@click.argument("text")
@clipboard_output
def d(text):
    """Decode base64."""
    try:
        return base64.b64decode(text.encode("utf-8")).decode("utf-8")
    except Exception as exc:  # pragma: no cover
        raise click.ClickException("Unable to decode: " + str(exc))


@b64.command(short_help="Encode strings to base64")
@click.argument("text")
@clipboard_output
def e(text):
    """Encode base64."""
    try:
        return base64.b64encode(text.encode("utf-8")).decode("utf-8")
    except Exception as exc:  # pragma: no cover
        raise click.ClickException("Unable to encode: " + str(exc))
