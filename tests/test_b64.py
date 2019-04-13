import base64

from click.testing import CliRunner

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.b64 import b64decode
from soh.b64 import b64encode
from .test_util import check_clipboard_output


@check_clipboard_output
def test_b64e(sample_text, clip):
    runner = CliRunner()

    # build args
    args = [sample_text]
    if clip is not None:
        args += [clip]

    result = runner.invoke(b64encode, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    assert output == base64.b64encode(sample_text.encode("utf-8")).decode("utf-8")

    return result


@check_clipboard_output
def test_b64d(sample_b64, clip):
    runner = CliRunner()

    # build args
    args = [sample_b64]
    if clip is not None:
        args += [clip]

    result = runner.invoke(b64decode, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    assert output == base64.b64decode(sample_b64.encode("utf-8")).decode("utf-8")

    return result
