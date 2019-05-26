"""JWT CLI functionality.

Entry point: $ soh jwt [OPTS] <text>
"""
import base64
import json

import click
import pyperclip

from soh.util import clipboard_output


def b64decode(segment):
    return base64.urlsafe_b64decode(segment + "=" * (len(segment) % 4)).decode("utf-8")


def segment_to_dict(segment):
    return json.loads(b64decode(segment))


@click.command(short_help="Display JWT contents")
@click.option("-i", "--indent", default=4, show_default=True, help="json indent")
@click.argument("token", required=False)
@clipboard_output
def jwt(indent, token):
    if token is None:  # pragma: no cover
        click.echo("No argument passed. Using clipboard contents...")
        token = pyperclip.paste()
    try:
        header, payload, signature = token.split(".")
        output = "header = " + json.dumps(segment_to_dict(header), indent=indent)
        output += "\n"
        output += "payload = " + json.dumps(segment_to_dict(payload), indent=indent)
        output += "\n"
        output += 'signature = "' + signature + '"'
        return output
    except Exception as exc:  # pragma: no cover
        raise click.ClickException(exc)


# TODO paseto
