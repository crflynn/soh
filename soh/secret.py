"""Secrets generation CLI functionality.

Entry point: $ soh secret b [OPTS]
Entry point: $ soh secret h [OPTS]
Entry point: $ soh secret u [OPTS]
Entry point: $ soh secret pw [OPTS]
"""
import random
import secrets
import string

import click

from soh.util import clipboard_output


AMBIGUOUS_CHARACTERS = "Iil1Lo0O"


@click.group(invoke_without_command=False, short_help="+ Secrets generators")
def secret():
    """Secrets generation."""
    pass  # pragma: no cover


@secret.command(short_help="Generate a urlsafe token")
@click.option("-b", "--bytes", "nbytes", default=32, show_default=True, help="number of bytes")
@clipboard_output
def u(nbytes):
    """Generate a urlsafe secret of n bytes."""
    return secrets.token_urlsafe(nbytes)


@secret.command(short_help="Generate a hex token")
@click.option("-b", "--bytes", "nbytes", default=32, show_default=True, help="number of bytes")
@clipboard_output
def h(nbytes):
    """Generate a urlsafe secret of n bytes."""
    return secrets.token_hex(nbytes)


@secret.command(short_help="Generate a bytes token")
@click.option("-b", "--bytes", "nbytes", default=32, show_default=True, help="number of bytes")
@clipboard_output
def b(nbytes):
    """Generate a urlsafe secret of n bytes."""
    return str(secrets.token_bytes(nbytes))[2:-1]


@secret.command(short_help="Generate a password")
@click.option("-n", default=8, show_default=True, help="quantity of numbers")
@click.option("-s", default=4, show_default=True, help="quantity of symbols")
@click.option("-l", default=32, show_default=True, help="length")
@click.option("-a", is_flag=True, default=False, show_default=True, help="allow ambiguous characters (Iil1Lo0O)")
@click.option("-p", "--protect", "protect", is_flag=True, default=False, show_default=True, help="hide from console")
@clipboard_output
def pw(n, s, l, a):
    """Generate a password."""
    if n + s > l:
        raise click.ClickException("Password length must exceed character requirements.")

    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # avoid ambiguous characters
    if a is False:
        table = str.maketrans(dict.fromkeys(AMBIGUOUS_CHARACTERS))
        letters = letters.translate(table)
        numbers = numbers.translate(table)
        symbols = symbols.translate(table)

    password = "".join(secrets.choice(numbers) for _ in range(n))
    password += "".join(secrets.choice(symbols) for _ in range(s))
    password += "".join(secrets.choice(letters) for _ in range(l - n - s))

    password = list(password)
    random.shuffle(password)

    return "".join(password)
