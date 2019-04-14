import ipaddress
import multiprocessing
import platform
import socket
from uuid import getnode

from click.testing import CliRunner
import vcr

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.sys import sys
from soh.sys import mac
from soh.sys import ip
from soh.sys import eip
from soh.sys import proc
from soh.sys import cores
from soh.sys import machine
from soh.sys import version
from soh.sys import node
from soh.sys import arch
from .test_util import check_clipboard_output


# @check_clipboard_output
def test_sys(float_):  # , clip):
    # TODO
    pass


# @check_clipboard_output
def test_sys_mac(upper):  # , clip):
    args = []
    if upper is not None:
        args += [upper]

    compare_to = ":".join(("%012X" % getnode())[i : i + 2] for i in range(0, 12, 2))
    if upper:
        compare_to = compare_to.upper()

    check_sys_funcs(mac, args, compare_to)


# @check_clipboard_output
def test_sys_ip():  # , clip):
    args = []
    result = check_sys_funcs(ip, args, socket.gethostbyname(socket.gethostname()))
    value = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    address = ipaddress.ip_address(value)
    assert address.is_private


# @check_clipboard_output
def test_sys_eip():  # , clip):
    args = []
    with vcr.use_cassette("tests/cassettes/sys_eip.yaml"):
        result = check_sys_funcs(eip, args)
    value = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    address = ipaddress.ip_address(value)
    assert address.is_global


# @check_clipboard_output
def test_sys_proc():  # , clip):
    args = []
    check_sys_funcs(proc, args, platform.processor())


# @check_clipboard_output
def test_sys_cores():  # , clip):
    args = []
    check_sys_funcs(cores, args, str(multiprocessing.cpu_count()))


# @check_clipboard_output
def test_sys_machine():  # , clip):
    args = []
    check_sys_funcs(machine, args, platform.machine())


# @check_clipboard_output
def test_sys_version():  # , clip):
    args = []
    check_sys_funcs(version, args, platform.version())


# @check_clipboard_output
def test_sys_node():  # , clip):
    args = []
    check_sys_funcs(node, args, platform.node())


# @check_clipboard_output
def test_sys_arch():  # , clip):
    args = []
    check_sys_funcs(arch, args, "; ".join(platform.architecture()))


def check_sys_funcs(func, args, compare_to=None, clip=None):
    runner = CliRunner()

    result = runner.invoke(func, args)

    assert result.exit_code == 0

    if compare_to is not None:
        output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
        assert output.lower() == compare_to.lower()

    return result
