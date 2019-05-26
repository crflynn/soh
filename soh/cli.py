"""CLI functionality.

Entry point: $ soh --help
Entry point: $ soh version
"""
import click

from soh.b64 import b64
from soh.create import create
from soh.datetime import dt
from soh.epoch import epoch
from soh.serve import serve
from soh.json import json_
from soh.secret import secret
from soh.system import sys
from soh.tokens import jwt
from soh.uuid import uuid_
from soh.util import clipboard_output
from soh.__version__ import __version__


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """Sleight of hand CLI commands.

    (+) indicates command group.
    Use the -c flag on most commands to copy output to clipboard
    """
    pass  # pragma: no cover


@click.command(short_help="soh CLI version")
@clipboard_output
def version():
    """Sleight of hand (soh) version."""
    return __version__


cli.add_command(b64, name="b64")
cli.add_command(create, name="create")
cli.add_command(dt, name="dt")
cli.add_command(epoch, name="epoch")
cli.add_command(json_, name="json")
cli.add_command(jwt, name="jwt")
cli.add_command(secret, name="secret")
cli.add_command(serve, name="serve")
cli.add_command(sys, name="sys")
cli.add_command(uuid_, name="uuid")
cli.add_command(version, name="version")


if __name__ == "__main__":
    cli()  # pragma: no cover
