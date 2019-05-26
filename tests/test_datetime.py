import time

from click.testing import CliRunner
from dateutil.zoneinfo import get_zonefile_instance
from freezegun import freeze_time

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.datetime import time
from soh.datetime import now
from soh.datetime import date
from soh.datetime import from_


FROZEN_TIME = "2019-06-09T04:20:00.123456+00:00"
FROZEN_TIME_SECONDS = "2019-06-09T04:20:00+00:00"
FROZEN_TIME_EPOCH = "1560054000"
FROZEN_TIME_EST = "2019-06-08T23:20:00.123456-05:00"
FROZEN_TIME_EST_SECONDS = "2019-06-08T23:20:00-05:00"


TIMEZONES = sorted(list(get_zonefile_instance().zones))


@freeze_time(FROZEN_TIME)
def test_now(tz_label, tz):
    runner = CliRunner()

    # build args
    args = []
    if tz_label is not None:
        args += [tz_label, tz]

    result = runner.invoke(now, args)

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    if tz_label is not None:
        if tz == "list":
            assert result.exit_code == 0
            assert "EST" in output
        elif tz == "EST":
            assert result.exit_code == 0
            assert output == FROZEN_TIME_EST
        elif tz in TIMEZONES:
            assert result.exit_code == 0
        else:
            assert result.exit_code != 0
    elif tz_label is None:
        assert result.exit_code == 0
        assert output == FROZEN_TIME


@freeze_time(FROZEN_TIME)
def test_today(tz_label, tz):
    runner = CliRunner()

    # build args
    args = []
    if tz_label is not None:
        args += [tz_label, tz]

    result = runner.invoke(date, args)

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    if tz_label is not None:
        if tz == "list":
            assert result.exit_code == 0
            assert "EST" in output
        elif tz == "EST":
            assert result.exit_code == 0
            assert output == FROZEN_TIME_EST[:10]
        elif tz in TIMEZONES:
            assert result.exit_code == 0
        else:
            assert result.exit_code != 0
    elif tz_label is None:
        assert result.exit_code == 0
        assert output == FROZEN_TIME[:10]


@freeze_time(FROZEN_TIME)
def test_time(tz_label, tz):
    runner = CliRunner()

    # build args
    args = []
    if tz_label is not None:
        args += [tz_label, tz]

    result = runner.invoke(time, args)

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    if tz_label is not None:
        if tz == "list":
            assert result.exit_code == 0
            assert "EST" in output
        elif tz == "EST":
            assert result.exit_code == 0
            assert output == FROZEN_TIME_EST[11:]
        elif tz in TIMEZONES:
            assert result.exit_code == 0
        else:
            assert result.exit_code != 0
    elif tz_label is None:
        assert result.exit_code == 0
        assert output == FROZEN_TIME[11:]


def test_from(tz_label, tz):
    runner = CliRunner()

    # build args
    args = [FROZEN_TIME_EPOCH]
    if tz_label is not None:
        args += [tz_label, tz]

    result = runner.invoke(from_, args)

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    if tz_label is not None:
        if tz == "list":
            assert result.exit_code == 0
            assert "EST" in output
        elif tz == "EST":
            print(args)
            assert result.exit_code == 0
            assert output == FROZEN_TIME_EST_SECONDS
        elif tz in TIMEZONES:
            assert result.exit_code == 0
        else:
            assert result.exit_code != 0
    elif tz_label is None:
        assert result.exit_code == 0
        assert output == FROZEN_TIME_SECONDS
