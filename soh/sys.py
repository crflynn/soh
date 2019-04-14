import multiprocessing
import platform
import socket
from uuid import getnode

import click
import requests

from soh.util import clipboard_output


@click.group(invoke_without_command=True, short_help="System information")
@click.pass_context
@clipboard_output
def sys(ctx):
    """System information."""
    if ctx.invoked_subcommand is None:
        # TODO complete set of info here (?)
        return platform.system()
    return ""  # pragma: no cover


@sys.command(short_help="Local MAC address")
@click.option("-u", "--upper", is_flag=True, help="use upper case")
@clipboard_output
def mac(upper):
    """MAC address."""
    node = getnode()
    value = ":".join(("%012X" % node)[i : i + 2] for i in range(0, 12, 2))

    if upper:
        value = value.upper()

    return str(value)


@sys.command(short_help="Local IP address")
@clipboard_output
def ip():
    """Local IP address."""
    value = socket.gethostbyname(socket.gethostname())
    return str(value)


@sys.command(short_help="External IP address")
@clipboard_output
def eip():
    """External IP address."""
    response = requests.get("https://api6.ipify.org?format=json")
    try:
        response.raise_for_status()
    except requests.RequestException:
        raise click.ClickException("External request failed.")  # pragma: no cover

    value = response.json()["ip"]

    return value


@sys.command(short_help="Processor information")
@clipboard_output
def proc():
    """Processor."""
    return platform.processor()


@sys.command(short_help="Number of cores")
@clipboard_output
def cores():
    """Number of cores."""
    return str(multiprocessing.cpu_count())


@sys.command(short_help="Machine information")
@clipboard_output
def machine():
    """Machine type."""
    return platform.machine()


@sys.command(short_help="OS version")
@clipboard_output
def version():
    """System release version."""
    return platform.version()


@sys.command(short_help="OS version")
@clipboard_output
def node():
    """Node name."""
    return platform.node()


@sys.command(short_help="OS version")
@clipboard_output
def arch():
    """Node name."""
    return "; ".join(platform.architecture())
