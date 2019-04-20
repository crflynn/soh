"""System information.

Entry point: $ soh arch
Entry point: $ soh cores
Entry point: $ soh eip
Entry point: $ soh ip
Entry point: $ soh eip
Entry point: $ soh mac
Entry point: $ soh machine
Entry point: $ soh node
Entry point: $ soh proc
Entry point: $ soh sys
Entry point: $ soh sysver
"""
import multiprocessing
import platform
import socket
from uuid import getnode

import click
import requests

from soh.util import clipboard_output
from soh.util import ensure_ok_response


@click.command(short_help="OS version")
@clipboard_output
def arch():
    """Platform architecture."""
    return "; ".join(platform.architecture())


@click.command(short_help="Number of cores")
@clipboard_output
def cores():
    """Number of cores."""
    return str(multiprocessing.cpu_count())


@click.command(short_help="External IP address")
@clipboard_output
def eip():
    """External IP address."""
    response = requests.get("https://api6.ipify.org?format=json")
    ensure_ok_response(response, "External request failed.")

    value = response.json()["ip"]

    return value


@click.command(short_help="Local IP address")
@clipboard_output
def ip():
    """Local IP address."""
    value = socket.gethostbyname(socket.gethostname())
    return str(value)


@click.command(short_help="Local MAC address")
@click.option("-u", "--upper", is_flag=True, help="use upper case")
@clipboard_output
def mac(upper):
    """MAC address."""
    node = getnode()
    value = ":".join(("%012x" % node)[i : i + 2] for i in range(0, 12, 2))

    if upper:
        value = value.upper()

    return str(value)


@click.command(short_help="Machine information")
@clipboard_output
def machine():
    """Machine type."""
    return platform.machine()


@click.command(short_help="OS version")
@clipboard_output
def node():
    """Node name."""
    return platform.node()


@click.command(short_help="Processor information")
@clipboard_output
def proc():
    """Processor."""
    return platform.processor()


@click.command(short_help="System information")
@clipboard_output
def sys():
    """System information."""
    return platform.system()


@click.command(short_help="OS version")
@clipboard_output
def sysver():
    """System release version."""
    return platform.version()
