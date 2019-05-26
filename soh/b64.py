"""Base64 CLI functionality.

Entry point: $ soh b64d [OPTS] <text>
Entry point: $ soh b64e [OPTS] <text>
"""
import base64

import click
import pyperclip

from soh.util import clipboard_output


def apply_padding(text):
    return text + "=" * (len(text) % 4)


@click.group(invoke_without_command=False, short_help="+ Base64 operations")
def b64():
    """Base64 decoding and encoding."""
    pass  # pragma: no cover


@b64.command(short_help="Decode base64 strings")
@click.option("-p", "--pad", is_flag=True, default=False, show_default=True, help="try to apply missing padding")
@click.argument("text", required=False)
@clipboard_output
def d(text, pad):
    """Decode base64 to text.

    If `text` argument is missing, uses clipboard contents.
    """
    if text is None:  # pragma: no cover
        click.echo("No argument passed. Using clipboard contents...")
        text = pyperclip.paste()
    if pad:
        text = apply_padding(text)
    try:
        return base64.b64decode(text.encode("utf-8")).decode("utf-8")
    except Exception as exc:  # pragma: no cover
        raise click.ClickException("Unable to decode: " + str(exc))


@b64.command(short_help="Encode strings to base64")
@click.argument("text", required=False)
@clipboard_output
def e(text):
    """Encode text to base64.

    If `text` argument is missing, uses clipboard contents.
    """
    if text is None:  # pragma: no cover
        click.echo("No argument passed. Using clipboard contents...")
        text = pyperclip.paste()
    try:
        return base64.b64encode(text.encode("utf-8")).decode("utf-8")
    except Exception as exc:  # pragma: no cover
        raise click.ClickException("Unable to encode: " + str(exc))
