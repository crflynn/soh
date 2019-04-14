import time

from click.testing import CliRunner

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.epoch import epoch
from soh.epoch import s
from soh.epoch import ms
from soh.epoch import us
from soh.epoch import ns
from .test_util import check_clipboard_output


# @check_clipboard_output
def test_epoch(float_):  # , clip):
    print("epoch")
    return check_epochs(epoch, float_, divisor=10 ** 9)


# @check_clipboard_output
def test_epoch_s(float_):  # , clip):
    print("epoch s")
    return check_epochs(s, float_, divisor=10 ** 9)


# @check_clipboard_output
def test_epoch_ms(float_):  # , clip):
    print("epoch ms")
    return check_epochs(ms, float_, divisor=10 ** 6)


# @check_clipboard_output
def test_epoch_us(float_):  # , clip):
    print("epoch us")
    return check_epochs(us, float_, divisor=10 ** 3)


# @check_clipboard_output
def test_epoch_ns(float_):  # , clip):
    print("epoch ns")
    return check_epochs(ns, float_, divisor=1)


def check_epochs(func, float_, divisor, clip=None):
    runner = CliRunner()

    # build args
    args = []
    if float_ is not None:
        args += [float_]
    # if clip is not None:
    #     args += [clip]

    result = runner.invoke(func, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    assert time.time_ns() / divisor - float(output) < 1 * 10 ** 9 / divisor

    if float_ and func != ns:
        assert "." in output
    else:
        assert "." not in output

    return result
