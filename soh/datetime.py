"""System information.

Entry point: $ soh utcnow
"""
import datetime

import click

from soh.util import clipboard_output


# TODO utc vs local
# TODO timezones


@click.command(short_help="OS version")
@click.option("-t", is_flag=True, default=False, help="use T separator")
@clipboard_output
def now(t):
    """Current datetime."""
    if t:
        return datetime.datetime.utcnow().isoformat("T")
    else:
        return str(datetime.datetime.utcnow())


@click.command(short_help="OS version")
@clipboard_output
def time():
    """Current time."""
    return str(datetime.datetime.utcnow())[11:]


# TODO use T sep
@click.command(short_help="OS version")
@clipboard_output
def today():
    """Current date."""
    return str(datetime.date.today())
