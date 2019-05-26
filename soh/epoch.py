"""Epoch time functionality.

Entry point: $ soh epoch [OPTS]
Entry point: $ soh epoch s [OPTS]
Entry point: $ soh epoch ms [OPTS]
Entry point: $ soh epoch us [OPTS]
Entry point: $ soh epoch ns [OPTS]
"""
import sys
import time

import arrow
import click

from soh.util import clipboard_output


@click.group(invoke_without_command=False, short_help="+ Epoch times")
def epoch():
    """Epoch times."""
    pass  # pragma: no cover


@epoch.command(short_help="epoch time seconds")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def s(float_):
    """Epoch time in seconds."""
    value = time.time()

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="epoch time milliseconds")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def ms(float_):
    """Epoch time in milliseconds."""
    if sys.version_info < (3, 6):
        value = time.time() * 10 ** 3
    else:
        value = time.time_ns() / 10 ** 6

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="epoch time microseconds")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def us(float_):
    """Epoch time in microseconds."""
    if sys.version_info < (3, 6):
        value = time.time() * 10 ** 6
    else:
        value = time.time_ns() / 10 ** 3

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="epoch time nanoseconds")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def ns(float_):
    """Epoch time in nanoseconds."""
    if sys.version_info < (3, 6):
        value = time.time() * 10 ** 9
    else:
        value = time.time_ns()

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(name="from", short_help="epoch time from a timestamp")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@click.argument("datetime")
@clipboard_output
def from_(float_, datetime):
    """Epoch time from a timestamp (in quotes)."""
    try:
        if float_:
            return str(arrow.get(datetime).float_timestamp)
        else:
            return str(arrow.get(datetime).timestamp)
    except Exception as exc:
        raise click.ClickException(exc)
