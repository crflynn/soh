"""Epoch time functionality.

Entry point: $ soh epoch [OPTS]
Entry point: $ soh epoch s [OPTS]
Entry point: $ soh epoch ms [OPTS]
Entry point: $ soh epoch us [OPTS]
Entry point: $ soh epoch ns [OPTS]
"""
import time

import click

from soh.util import clipboard_output


# TODO consider `epoch` invoke without command = false


@click.group(invoke_without_command=True, short_help="Epoch times")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@click.pass_context
@clipboard_output
def epoch(ctx, float_):
    """Epoch time in seconds."""
    if ctx.invoked_subcommand is None:
        value = time.time_ns() / 10 ** 9
        if not float_:
            value = int(value)
        return str(value)
    return ""  # pragma: no cover


@epoch.command(short_help="epoch time seconds")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def s(float_):
    """Epoch time in seconds."""
    value = time.time_ns() / 10 ** 9

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="epoch time milliseconds")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def ms(float_):
    """Epoch time in milliseconds."""
    value = time.time_ns() / 10 ** 6

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="epoch time microseconds")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def us(float_):
    """Epoch time in microseconds."""
    value = time.time_ns() / 10 ** 3

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="epoch time nanoseconds")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def ns(float_):
    """Epoch time in nanoseconds."""
    value = time.time_ns()

    if not float_:
        value = int(value)

    return str(value)
