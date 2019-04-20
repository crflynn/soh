import json

from click.testing import CliRunner

from soh.util import COPIED_TO_CLIPBOARD_MESSAGE
from soh.tokens import jwt


def test_jwt(indent_label, indent, jwt_sample):
    runner = CliRunner()
    # build args
    args = []
    if indent_label is not None:
        args += [indent_label, indent]
    else:
        indent = 4
    args += [jwt_sample]

    result = runner.invoke(jwt, args)

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0]
    print(output)

    if indent_label is not None:
        for row in output.split("\n"):
            print(row, len(row), len(row.lstrip()))
            assert (len(row) - len(row.lstrip())) % indent == 0

    header = {"alg": "HS256", "typ": "JWT"}
    payload = {"sub": "1234567890", "name": "John Doe", "iat": 1516239022}
    signature = "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

    assert json.dumps(header, indent=indent) in output
    assert json.dumps(payload, indent=indent) in output
    assert signature in output
