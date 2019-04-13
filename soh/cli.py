"""CLI functionality.

Entry point: $ soh [CMD] [OPTS] input
"""
import click

from soh.b64 import b64decode
from soh.b64 import b64encode
from soh.uuid import uuid


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


cli.add_command(b64decode, name="b64d")
cli.add_command(b64encode, name="b64e")
cli.add_command(uuid, name="uuid")


if __name__ == "__main__":
    cli()
