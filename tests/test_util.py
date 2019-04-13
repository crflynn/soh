from functools import wraps

import click
from click.testing import CliRunner
import pyperclip

from soh.util import clipboard_output
from soh.util import COPIED_TO_CLIPBOARD_MESSAGE


CLIPBOARD_TEST_VALUE = "qweoridvlasna;ebvaubv"


def check_clipboard_output(func):
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


@check_clipboard_output
def test_dummy(clip):
    runner = CliRunner()
    args = [clip]
    result = runner.invoke(dummy, [a for a in args if a is not None])
    assert result.exit_code == 0
    return result
