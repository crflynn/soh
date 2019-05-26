"""JSON printing CLI functionality.

Entry point: $ soh json [OPTS] <text>
"""
import json

import click
import pyperclip

from soh.util import clipboard_output


@click.command(short_help="JSON printing")
@click.option("-i", "--indent", default=4, help="indent quantity")
@click.option("-a", "--ascii", "ascii_", is_flag=True, default=False, help="ensure ascii")
@click.argument("text", required=False)
@clipboard_output
def json_(indent, text, ascii_):
    """JSON printing.

    Use single quotes around the JSON text.
    """
    if text is None:  # pragma: no cover
        click.echo("No argument passed. Using clipboard contents...")
        text = pyperclip.paste()
    try:
        return json.dumps(json.loads(text), indent=indent, ensure_ascii=ascii_)
    except json.decoder.JSONDecodeError:
        raise click.ClickException("Unable to parse JSON.")
