"""CLI functionality.

Entry point: $ soh [CMD] [OPTS] input
"""
import click

from soh.b64 import b64decode
from soh.b64 import b64encode
from soh.epoch import epoch
from soh.uuid import uuid_


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass  # pragma: no cover


cli.add_command(b64decode, name="b64d")
cli.add_command(b64encode, name="b64e")
cli.add_command(epoch, name="epoch")
cli.add_command(uuid_, name="uuid")


if __name__ == "__main__":
    cli()  # pragma: no cover
