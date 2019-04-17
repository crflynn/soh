"""CLI functionality.

Entry point: $ soh --help
Entry point: $ soh version
"""
import click

from soh.b64 import b64
from soh.create import create
from soh.create import gitignore
from soh.epoch import epoch
from soh.system import arch
from soh.system import cores
from soh.system import eip
from soh.system import ip
from soh.system import mac
from soh.system import machine
from soh.system import node
from soh.system import proc
from soh.system import sys
from soh.system import sysver
from soh.tokens import jwt
from soh.uuid import uuid_
from soh.util import clipboard_output
from soh.__version__ import __version__


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """Sleight of hand CLI tricks."""
    pass  # pragma: no cover


@click.command()
@clipboard_output
def version():
    """Sleight of hand (soh) version."""
    return __version__


cli.add_command(b64, name="b64")
cli.add_command(create, name="create")
cli.add_command(gitignore, name="gitignore")
cli.add_command(epoch, name="epoch")
cli.add_command(arch, name="arch")
cli.add_command(cores, name="cores")
cli.add_command(eip, name="eip")
cli.add_command(ip, name="ip")
cli.add_command(jwt, name="jwt")
cli.add_command(mac, name="mac")
cli.add_command(machine, name="machine")
cli.add_command(node, name="node")
cli.add_command(proc, name="proc")
cli.add_command(sys, name="sys")
cli.add_command(sysver, name="sysver")
cli.add_command(uuid_, name="uuid")
cli.add_command(version, name="version")


if __name__ == "__main__":
    cli()  # pragma: no cover
