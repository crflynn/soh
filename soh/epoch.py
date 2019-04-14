import time

import click

from soh.util import clipboard_output


@click.group(invoke_without_command=True)
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@click.pass_context
@clipboard_output
def epoch(ctx, float_):
    if ctx.invoked_subcommand is None:
        value = time.time_ns() / 10 ** 9
        if not float_:
            value = int(value)
        return str(value)
    return ""


@epoch.command(short_help="Epoch times")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def s(float_):
    value = time.time_ns() / 10 ** 9

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="Epoch times")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def ms(float_):
    value = time.time_ns() / 10 ** 6

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="Epoch times")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def us(float_):
    value = time.time_ns() / 10 ** 3

    if not float_:
        value = int(value)

    return str(value)


@epoch.command(short_help="Epoch times")
@click.option("-f", "--float", "float_", is_flag=True, default=False, help="return float value")
@clipboard_output
def ns(float_):
    value = time.time_ns()

    if not float_:
        value = int(value)

    return str(value)
