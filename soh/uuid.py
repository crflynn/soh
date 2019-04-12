"""UUID CLI functionality.

Entry point: $ soh uuid [OPTS]
"""
import uuid as _uuid

import click
import pyperclip


@click.command(short_help="Generate UUIDs")
@click.option("-v", "--version", default=4, show_default=True, help="uuid version")
@click.option("-ns", "--namespace", help="namespace (v3, v5) {dns, url, oid, x500}")
@click.option("-n", "--name", default="", help="name (v3, v5)")
@click.option("-u", "--upper", is_flag=True, help="use upper case")
@click.option("-c", "--clip", is_flag=True, help="copy to clipboard")
def uuid(version, namespace, name, upper, clip):
    """Generate UUIDs."""
    if namespace is not None:
        namespaces = {
            "dns": _uuid.NAMESPACE_DNS,
            "url": _uuid.NAMESPACE_URL,
            "oid": _uuid.NAMESPACE_OID,
            "x500": _uuid.NAMESPACE_X500,
        }
        try:
            ns = namespaces[namespace.lower()]
        except KeyError:
            raise click.ClickException("Invalid namespace, must be in {dns, url, oid, x500}")
    elif version in (3, 5):
        raise click.ClickException(f"Namespace must be provided for version {version}")

    if version == 1:
        value = str(_uuid.uuid1())
    elif version == 3:
        value = str(_uuid.uuid3(ns, name))
    elif version == 4:
        value = str(_uuid.uuid4())
    elif version == 5:
        value = str(_uuid.uuid5(ns, name))
    else:
        raise click.ClickException("Invalid version")

    if upper:
        value = value.upper()

    if clip:
        click.secho(value, fg="yellow")
        pyperclip.copy(value)
    else:
        click.secho(value)
