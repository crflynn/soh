"""UTC Datetime information.

Entry point: $ soh now [OPTS]
Entry point: $ soh time [OPTS]
Entry point: $ soh today [OPTS]
"""
import datetime

import click

from soh.util import clipboard_output


# TODO utc vs local
# TODO timezones
# TODO consider moving these commands under a `dt` command


@click.command(short_help="UTC now")
@click.option("-t", is_flag=True, default=False, help="use T separator")
@clipboard_output
def now(t):
    """Current datetime."""
    if t:
        return datetime.datetime.utcnow().isoformat("T")
    else:
        return str(datetime.datetime.utcnow())


@click.command(short_help="UTC time")
@clipboard_output
def time():
    """Current time."""
    return str(datetime.datetime.utcnow())[11:]


# TODO use T sep
@click.command(short_help="UTC date")
@clipboard_output
def today():
    """Current date."""
    return str(datetime.date.today())
