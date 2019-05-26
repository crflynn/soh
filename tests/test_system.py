import ipaddress
import multiprocessing
import platform
import socket
from uuid import getnode

import vcr
from click.testing import CliRunner

from .common import compare
from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.system import all_
from soh.system import arch
from soh.system import cores
from soh.system import eip
from soh.system import ip
from soh.system import mac
from soh.system import machine
from soh.system import node
from soh.system import platform_
from soh.system import proc
from soh.system import version
from .test_util import check_clipboard_output


def test_all():
    runner = CliRunner()
    args = []

    result = runner.invoke(all_, args)

    assert result.exit_code == 0


# @check_clipboard_output
def test_arch():  # , clip):
    args = []
    compare(arch, args, "; ".join(platform.architecture()))


# @check_clipboard_output
def test_cores():  # , clip):
    args = []
    compare(cores, args, str(multiprocessing.cpu_count()))


# @check_clipboard_output
def test_eip():  # , clip):
    args = []
    with vcr.use_cassette("tests/cassettes/system_eip.yaml"):
        result = compare(eip, args)
    value = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    address = ipaddress.ip_address(value)
    assert address.is_global


# @check_clipboard_output
def test_ip():  # , clip):
    args = []
    result = compare(ip, args, socket.gethostbyname(socket.gethostname()))
    value = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    address = ipaddress.ip_address(value)
    assert address.is_private


# @check_clipboard_output
def test_mac(upper):  # , clip):
    args = []
    if upper is not None:
        args += [upper]

    compare_to = ":".join(("%012x" % getnode())[i : i + 2] for i in range(0, 12, 2))
    if upper:
        compare_to = compare_to.upper()

    compare(mac, args, compare_to)


# @check_clipboard_output
def test_machine():  # , clip):
    args = []
    compare(machine, args, platform.machine())


# @check_clipboard_output
def test_node():  # , clip):
    args = []
    compare(node, args, platform.node())


# @check_clipboard_output
def test_platform():  # , clip):
    args = []
    compare(platform_, args, platform.system())


# @check_clipboard_output
def test_proc():  # , clip):
    args = []
    compare(proc, args, platform.processor())


# @check_clipboard_output
def test_version():  # , clip):
    args = []
    compare(version, args, platform.version())
