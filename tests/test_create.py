import os
import uuid

from click.testing import CliRunner
import vcr

from soh.create import gitignore
from soh import create
from soh.util import COPIED_TO_CLIPBOARD_MESSAGE


def test_gitignore(overwrite, language):
    # patch over the gitignore name so we don't overwrite the actual .gitignore
    # use randomness in the name in order to parallelized tests
    create.GITIGNORE_FILE = f"{str(uuid.uuid4())}.gitignore"

    runner = CliRunner()

    # build args
    args = []
    if overwrite is not None:
        args += [overwrite]
    args += [language]

    with vcr.use_cassette(f"tests/cassettes/create_gitignore_{language}.yaml"):
        result = runner.invoke(gitignore, args)

    if language == "invalid_language":
        assert result.exit_code != 0
        return

    assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")

    if language == "list":
        assert "python" in output
        return
    else:
        assert os.path.isfile(create.GITIGNORE_FILE)

    # test overwrite functionality
    with vcr.use_cassette(f"tests/cassettes/create_gitignore_{language}.yaml"):
        result = runner.invoke(gitignore, args)

    if overwrite is None:
        assert result.exit_code != 0
    elif overwrite in ("-o", "--overwrite"):
        assert result.exit_code == 0

    assert os.path.isfile(create.GITIGNORE_FILE)

    # cleanup
    os.remove(create.GITIGNORE_FILE)