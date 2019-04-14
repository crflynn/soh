"""CLI functionality.

Entry point: $ soh [CMD] [OPTS] input
"""
import click

from soh.b64 import b64
from soh.epoch import epoch
from soh.tokens import jwt
from soh.uuid import uuid_


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """Sleight of hand CLI tricks."""
    pass  # pragma: no cover


cli.add_command(b64, name="b64")
cli.add_command(epoch, name="epoch")
cli.add_command(jwt, name="jwt")
cli.add_command(uuid_, name="uuid")


if __name__ == "__main__":
    cli()  # pragma: no cover
