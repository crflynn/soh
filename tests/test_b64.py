import base64

from click.testing import CliRunner

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.b64 import d
from soh.b64 import e


def test_b64e(sample_text):
    runner = CliRunner()

    # build args
    args = [sample_text]

    result = runner.invoke(e, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    assert output == base64.b64encode(sample_text.encode("utf-8")).decode("utf-8")

    return result


def test_b64d(sample_b64, pad):
    runner = CliRunner()

    # build args
    args = [sample_b64]
    if pad is not None:
        args += [pad]

    result = runner.invoke(d, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    assert output == base64.b64decode(sample_b64.encode("utf-8")).decode("utf-8")

    return result
