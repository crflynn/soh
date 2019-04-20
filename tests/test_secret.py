import codecs
import string

from click.testing import CliRunner

from soh.secret import AMBIGUOUS_CHARACTERS
from soh.secret import b
from soh.secret import h
from soh.secret import pw
from soh.secret import u
from soh.util import COPIED_TO_CLIPBOARD_MESSAGE


def test_secret_b(nbytes_label, nbytes):
    runner = CliRunner()

    # build args
    args = []
    if nbytes_label is not None:
        args += [nbytes_label, nbytes]

    result = runner.invoke(b, args)

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")

    # output is a string representation of bytes
    # so we have to unescape it to it's original representation
    if nbytes_label:
        assert len(codecs.decode(output, "unicode_escape")) == nbytes
    else:
        assert len(codecs.decode(output, "unicode_escape")) == 32


def test_secret_h(nbytes_label, nbytes):
    runner = CliRunner()

    # build args
    args = []
    if nbytes_label is not None:
        args += [nbytes_label, nbytes]

    result = runner.invoke(h, args)

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")

    if nbytes_label:
        assert len(output) == nbytes * 2
    else:
        assert len(output) == 32 * 2


def test_secret_u(nbytes_label, nbytes):
    runner = CliRunner()

    # build args
    args = []
    if nbytes_label is not None:
        args += [nbytes_label, nbytes]

    result = runner.invoke(u, args)

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")

    # base64 encoding generates ~33% overhead
    if nbytes_label:
        assert len(output) > nbytes * 1.3
        assert len(output) < nbytes * 1.4
    else:
        assert len(output) > 32 * 1.3
        assert len(output) < 32 * 1.4


def test_secret_pw(qty_num_label, qty_num, qty_sym_label, qty_sym, length_label, length, allow_ambiguous, protect):
    runner = CliRunner()

    # build args
    args = []
    if qty_num_label is not None:
        args += [qty_num_label, qty_num]
    if qty_sym_label is not None:
        args += [qty_sym_label, qty_sym]
    if length_label is not None:
        args += [length_label, length]
    if allow_ambiguous is not None:
        args += [allow_ambiguous]
    if protect is not None:
        args += [protect]

    result = runner.invoke(pw, args)

    num = qty_num if qty_num_label is not None else 8
    sym = qty_sym if qty_sym_label is not None else 4
    lth = length if length_label is not None else 32

    if num + sym > lth:
        assert result.exit_code != 0
        return
    else:
        assert result.exit_code == 0

    output = result.output.rsplit(COPIED_TO_CLIPBOARD_MESSAGE)[0].replace("\n", "")

    if protect is not None:
        assert len(output) == 0
        return

    if length_label is not None:
        assert len(output) == length

    num_count = 0
    sym_count = 0
    for c in output:
        if c in string.digits:
            num_count += 1
        elif c in string.punctuation:
            sym_count += 1

    assert num_count == num
    assert sym_count == sym

    if allow_ambiguous is None:
        for c in AMBIGUOUS_CHARACTERS:
            assert c not in output
