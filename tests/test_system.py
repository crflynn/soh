import ipaddress
import multiprocessing
import platform
import socket
from uuid import getnode

from click.testing import CliRunner
import vcr

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
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
from .test_util import check_clipboard_output


# @check_clipboard_output
def test_arch():  # , clip):
    args = []
    check_system_funcs(arch, args, "; ".join(platform.architecture()))


# @check_clipboard_output
def test_cores():  # , clip):
    args = []
    check_system_funcs(cores, args, str(multiprocessing.cpu_count()))


# @check_clipboard_output
def test_eip():  # , clip):
    args = []
    with vcr.use_cassette("tests/cassettes/sys_eip.yaml"):
        result = check_system_funcs(eip, args)
    value = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    address = ipaddress.ip_address(value)
    assert address.is_global


# @check_clipboard_output
def test_ip():  # , clip):
    args = []
    result = check_system_funcs(ip, args, socket.gethostbyname(socket.gethostname()))
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

    check_system_funcs(mac, args, compare_to)


# @check_clipboard_output
def test_machine():  # , clip):
    args = []
    check_system_funcs(machine, args, platform.machine())


# @check_clipboard_output
def test_node():  # , clip):
    args = []
    check_system_funcs(node, args, platform.node())


# @check_clipboard_output
def test_proc():  # , clip):
    args = []
    check_system_funcs(proc, args, platform.processor())


# @check_clipboard_output
def test_sys():  # , clip):
    args = []
    check_system_funcs(sys, args, platform.system())


# @check_clipboard_output
def test_sysver():  # , clip):
    args = []
    check_system_funcs(sysver, args, platform.version())


def check_system_funcs(func, args, compare_to=None, clip=None):
    runner = CliRunner()

    result = runner.invoke(func, args)

    assert result.exit_code == 0

    if compare_to is not None:
        output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
        assert output == compare_to

    return result
