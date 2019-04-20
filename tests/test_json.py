import json

from click.testing import CliRunner

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.json import json_


def test_json(indent_label, indent, ascii_, json_text):
    runner = CliRunner()

    # build args
    args = []
    if indent_label is not None:
        args += [indent_label, indent]
    if ascii_ is not None:
        args += [ascii_]
    args += [json_text]

    result = runner.invoke(json_, args)

    try:
        json.loads(json_text)
    except json.decoder.JSONDecodeError:
        assert result.exit_code != 0
        return

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")
    if indent_label is not None:
        for row in output.split("\n"):
            assert (len(row) - len(row.lstrip())) % indent == 0
    if ascii_:
        assert output != json.dumps(json.loads(json_text), indent=indent, ensure_ascii=False)
    assert output == json.dumps(json.loads(json_text), indent=indent, ensure_ascii=ascii_)
