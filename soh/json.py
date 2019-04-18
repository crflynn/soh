"""Base64 CLI functionality.

Entry point: $ soh json [OPTS] <text>
"""
import json

import click

from soh.util import clipboard_output


@click.command(short_help="JSON printing")
@click.option("-i", "--indent", default=4, help="indent quantity")
@click.option("-a", "--ascii", is_flag=True, default=False, help="ensure ascii")
@click.argument("text")
@clipboard_output
def json_(indent, text, ascii):
    """JSON printing.

    Use single quotes around the JSON text.
    """
    try:
        return json.dumps(json.loads(text), indent=indent, ensure_ascii=ascii)
    except json.decoder.JSONDecodeError:
        raise click.ClickException("Unable to parse JSON.")
