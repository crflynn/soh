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


@click.group(invoke_without_command=False, short_help="+ System information")
def sys():
    """System information."""
    pass  # pragma: no cover


@sys.command(name="all", short_help="System information")
@clipboard_output
def all_():
    """System information"""
    return (
        "Arch: " + "; ".join(platform.architecture()) + "\n"
        "Cores: " + str(multiprocessing.cpu_count()) + "\n"
        "External IP: " + get_external_ip() + "\n"
        "Local IP: " + socket.gethostbyname(socket.gethostname()) + "\n"
        "MAC Address: " + ":".join(("%012x" % getnode())[i : i + 2] for i in range(0, 12, 2)) + "\n"
        "Machine type: " + platform.machine() + "\n"
        "Machine name: " + platform.node() + "\n"
        "Platform: " + platform.system() + "\n"
        "Platform version: " + platform.version() + "\n"
        "Processor: " + platform.processor()
    )


@sys.command(short_help="OS architecture")
@clipboard_output
def arch():
    """Platform architecture."""
    return "; ".join(platform.architecture())


@sys.command(short_help="Number of cores")
@clipboard_output
def cores():
    """Number of cores."""
    return str(multiprocessing.cpu_count())


@sys.command(short_help="External IP address")
@clipboard_output
def eip():
    """External IP address."""
    return get_external_ip()


def get_external_ip():
    response = requests.get("https://api6.ipify.org?format=json")
    ensure_ok_response(response, "External request failed.")

    value = response.json()["ip"]

    return value


@sys.command(short_help="Local IP address")
@clipboard_output
def ip():
    """Local IP address."""
    value = socket.gethostbyname(socket.gethostname())
    return str(value)


@sys.command(short_help="Local MAC address")
@click.option("-u", "--upper", is_flag=True, help="use upper case")
@clipboard_output
def mac(upper):
    """MAC address."""
    value = ":".join(("%012x" % getnode())[i : i + 2] for i in range(0, 12, 2))

    if upper:
        value = value.upper()

    return str(value)


@sys.command(short_help="Machine information")
@clipboard_output
def machine():
    """Machine type."""
    return platform.machine()


@sys.command(short_help="Machine name")
@clipboard_output
def node():
    """Node name."""
    return platform.node()


@sys.command(name="platform", short_help="Platform type")
@clipboard_output
def platform_():
    """Platform type."""
    return platform.system()


@sys.command(short_help="Processor information")
@clipboard_output
def proc():
    """Processor."""
    return platform.processor()


@sys.command(short_help="OS version")
@clipboard_output
def version():
    """System release version."""
    return platform.version()
