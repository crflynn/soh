import time

from click.testing import CliRunner
from freezegun import freeze_time

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.datetime import time
from soh.datetime import now
from soh.datetime import today


FROZEN_TIME = "2019-06-09 04:20:00.123456"


@freeze_time(FROZEN_TIME)
def test_now(t):
    runner = CliRunner()

    # build args
    args = []
    if t is not None:
        args += [t]
    # if clip is not None:
    #     args += [clip]

    result = runner.invoke(now, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    if t is not None:
        assert output == FROZEN_TIME.replace(" ", "T")
    else:
        assert output == FROZEN_TIME


@freeze_time(FROZEN_TIME)
def test_today():
    runner = CliRunner()

    # build args
    args = []
    # if clip is not None:
    #     args += [clip]

    result = runner.invoke(today, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    assert output == FROZEN_TIME[:10]


@freeze_time(FROZEN_TIME)
def test_time():
    runner = CliRunner()

    # build args
    args = []
    # if clip is not None:
    #     args += [clip]

    result = runner.invoke(time, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    assert output == FROZEN_TIME[11:]
