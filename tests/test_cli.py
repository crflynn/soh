from .common import compare
from soh.cli import version
from soh.__version__ import __version__


# @check_clipboard_output
def test_version():  # , clip):
    args = []
    compare(version, args, __version__)
