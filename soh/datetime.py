"""UTC Datetime information.

Entry point: $ soh now [OPTS]
Entry point: $ soh time [OPTS]
Entry point: $ soh today [OPTS]
"""
import arrow
from arrow.parser import ParserError
from dateutil.zoneinfo import get_zonefile_instance
import click

from soh.util import clipboard_output


@click.group(invoke_without_command=False, short_help="+ Datetimes")
def dt():
    """Base64 decoding and encoding."""
    pass  # pragma: no cover


def get_tz_time(time_, tz):
    if tz == "list":
        return "\n".join(sorted(list(get_zonefile_instance().zones)))
    if tz is not None:
        try:
            the_time = time_.to(tz)
        except ParserError:
            raise click.ClickException("Unknown timezone: " + tz)
    else:
        the_time = time_
    return the_time


@dt.command(short_help="UTC now")
@click.option("-tz", show_default=True, help="timezone")
@clipboard_output
def now(tz):
    """Current datetime."""
    return str(get_tz_time(arrow.utcnow(), tz))


@dt.command(short_help="UTC time")
@click.option("-tz", show_default=True, help="timezone")
@clipboard_output
def time(tz):
    """Current time."""
    if tz == "list":
        return str(get_tz_time(arrow.utcnow(), tz))
    else:
        return str(get_tz_time(arrow.utcnow(), tz))[11:]


@dt.command(short_help="UTC date")
@click.option("-tz", show_default=True, help="timezone")
@clipboard_output
def date(tz):
    """Current date."""
    if tz == "list":
        return str(get_tz_time(arrow.utcnow(), tz))
    else:
        return str(get_tz_time(arrow.utcnow(), tz).date())


@dt.command(name="from", short_help="Datetime from epoch seconds")
@click.option("-tz", show_default=True, help="timezone")
@click.argument("epoch")
@clipboard_output
def from_(tz, epoch):
    """Datetime from epoch seconds."""
    if tz == "list":
        return str(get_tz_time(arrow.get(epoch), tz))
    else:
        return str(get_tz_time(arrow.get(epoch), tz))
