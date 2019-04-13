from click.testing import CliRunner

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.uuid import uuid_
from .test_util import check_clipboard_output


@check_clipboard_output
def test_uuid(
    uuid_version_label, uuid_version, uuid_namespace_label, uuid_namespace, uuid_name_label, uuid_name, upper, clip
):
    runner = CliRunner()

    # build args
    args = []
    if uuid_version is not None:
        args += [uuid_version_label, uuid_version]
    if uuid_namespace is not None:
        args += [uuid_namespace_label, uuid_namespace]
    if uuid_name is not None:
        args += [uuid_name_label, uuid_name]
    if upper is not None:
        args += [upper]
    if clip is not None:
        args += [clip]

    result = runner.invoke(uuid_, [a for a in args if a is not None])

    # invalid combinations
    if uuid_version in (3, 5) and uuid_namespace is None:
        assert result.exit_code != 0
    else:
        assert result.exit_code == 0

    if upper is not None and result.exit_code == 0:
        msg = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0]
        assert msg == msg.upper()

    return result
