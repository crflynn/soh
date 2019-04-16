from click.testing import CliRunner

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE


def compare(func, args, compare_to=None, clip=None):
    runner = CliRunner()

    result = runner.invoke(func, args)

    assert result.exit_code == 0

    if compare_to is not None:
        output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
        assert output == compare_to

    return result
