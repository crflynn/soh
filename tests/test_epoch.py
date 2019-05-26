import sys
import time

import pytest
from click.testing import CliRunner

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.epoch import from_
from soh.epoch import s
from soh.epoch import ms
from soh.epoch import us
from soh.epoch import ns


FROZEN_TIME_SECONDS = "2019-06-09T04:20:00+00:00"
FROZEN_TIME_EPOCH = "1560054000"
NONSENSE_INPUT = "nonsense"
NONSENSE_OUTPUT = "nonsense"


def test_epoch_s(float_):
    return check_epochs(s, float_, divisor=10 ** 9)


def test_epoch_ms(float_):
    return check_epochs(ms, float_, divisor=10 ** 6)


def test_epoch_us(float_):
    return check_epochs(us, float_, divisor=10 ** 3)


def test_epoch_ns(float_):
    return check_epochs(ns, float_, divisor=1)


@pytest.mark.parametrize(
    "from_input,from_output", [(FROZEN_TIME_SECONDS, FROZEN_TIME_EPOCH), (NONSENSE_INPUT, NONSENSE_OUTPUT)]
)
def test_from(float_, from_input, from_output):
    runner = CliRunner()

    # build args
    args = [from_input]
    if float_ is not None:
        args += [float_]

    result = runner.invoke(from_, args)

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")

    if from_input == NONSENSE_INPUT:
        assert result.exit_code != 0
    else:
        assert result.exit_code == 0
        assert from_output in output


def check_epochs(func, float_, divisor):
    runner = CliRunner()

    # build args
    args = []
    if float_ is not None:
        args += [float_]

    result = runner.invoke(func, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    # assert less than one second has passed between now and invocation
    if sys.version_info < (3, 6):
        assert time.time() * 10 ** 9 / divisor - float(output) < 1 * 10 ** 9 / divisor
    else:
        assert time.time_ns() / divisor - float(output) < 1 * 10 ** 9 / divisor

    if float_ and func != ns:
        assert "." in output
    else:
        assert "." not in output

    return result
