from functools import wraps

import click
from click.testing import CliRunner
import pyperclip
import pytest
import requests
import vcr

from soh.util import clipboard_output
from soh.util import ensure_ok_response
from soh.util import COPIED_TO_CLIPBOARD_MESSAGE


CLIPBOARD_TEST_VALUE = "qweoridvlasna;ebvaubv"
FAILURE_MESSAGE = "fail message"


def check_clipboard_output(func):
    """Decorator to test clipboard output behavior.

    Doesn't work when running pytest xdist since parallelisation doesn't make sense
    with a single clipboard.
    """

    @wraps(func)
    def clipboard_checker(*args, **kwargs):
        pyperclip.copy(CLIPBOARD_TEST_VALUE)
        clip = kwargs.get("clip", None)

        result = func(*args, **kwargs)

        # only check clipboard results on success
        if result.exit_code != 0:
            return

        if clip is not None:
            assert COPIED_TO_CLIPBOARD_MESSAGE in result.output
            assert pyperclip.paste() != CLIPBOARD_TEST_VALUE
        else:
            assert COPIED_TO_CLIPBOARD_MESSAGE not in result.output
            assert pyperclip.paste() == CLIPBOARD_TEST_VALUE

    return clipboard_checker


@click.command(short_help="dummy command")
@clipboard_output
def dummy():
    return "something"


# @check_clipboard_output
def check_dummy(clip):
    runner = CliRunner()
    args = []
    if clip is not None:
        args += [clip]
    result = runner.invoke(dummy, args)
    assert result.exit_code == 0
    return result


def test_dummy():
    """Test the clipboard behavior serially."""
    for clip in [None, "-c", "--clip"]:
        pyperclip.copy(CLIPBOARD_TEST_VALUE)
        result = check_dummy(clip)
        if clip is not None:
            assert COPIED_TO_CLIPBOARD_MESSAGE in result.output
            assert pyperclip.paste() != CLIPBOARD_TEST_VALUE
        else:
            assert COPIED_TO_CLIPBOARD_MESSAGE not in result.output
            assert pyperclip.paste() == CLIPBOARD_TEST_VALUE


def test_ensure_ok_response():
    with vcr.use_cassette("tests/cassettes/util_success_response.yaml"):
        response = requests.get("https://httpbin.org/status/200")
        ensure_ok_response(response, FAILURE_MESSAGE)

    with vcr.use_cassette("tests/cassettes/util_fail_response.yaml"):
        response = requests.get("https://httpbin.org/status/500")
        with pytest.raises(click.ClickException) as exc:
            ensure_ok_response(response, FAILURE_MESSAGE)
            assert repr(exc) == FAILURE_MESSAGE
