"""JWT CLI functionality.

Entry point: $ soh b64d [OPTS] <text>
Entry point: $ soh b64e [OPTS] <text>
"""
import base64
import json

import click

from soh.util import clipboard_output


def b64decode(segment):
    return base64.urlsafe_b64decode(segment + "=" * (len(segment) % 4)).decode("utf-8")


def segment_to_dict(segment):
    return json.loads(b64decode(segment))


# TODO add verify option ? should just ust pyjwt for it with a secret param
@click.command(short_help="Display JWT contents")
@click.option("-i", "--indent", default=2, show_default=True, help="json indent")
@click.argument("token")
@clipboard_output
def jwt(token, indent):
    header, payload, signature = token.split(".")
    output = "header = " + json.dumps(segment_to_dict(header), indent=indent)
    output += "\n"
    output += "payload = " + json.dumps(segment_to_dict(payload), indent=indent)
    output += "\n"
    output += 'signature = "' + signature + '"'
    return output


# TODO paseto
