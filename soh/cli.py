"""CLI functionality.

Entry point: $ soh [CMD] [OPTS] input
"""
import click

from soh.uuid import uuid


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


cli.add_command(uuid, name="uuid")


if __name__ == "__main__":
    cli()
