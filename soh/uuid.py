"""UUID CLI functionality.

Entry point: $ soh uuid [OPTS]
"""
import uuid

import click

from soh.util import clipboard_output


@click.command(short_help="Generate UUIDs")
@click.option("-v", "--version", "uuid_version", default=4, show_default=True, help="uuid version {1, 3, 4, 5}")
@click.option("-ns", "--namespace", "uuid_namespace", help="namespace (for v3, v5) {dns, url, oid, x500}")
@click.option("-n", "--name", "uuid_name", default="", help="name (for v3, v5)")
@click.option("-u", "--upper", is_flag=True, help="use upper case")
@clipboard_output
def uuid_(uuid_version, uuid_namespace, uuid_name, upper):
    """Generate UUIDs."""
    if uuid_namespace is not None:
        if uuid_version not in (3, 5):
            raise click.ClickException("Namespaces only valid for versions {3, 5}")
        namespaces = {
            "dns": uuid.NAMESPACE_DNS,
            "url": uuid.NAMESPACE_URL,
            "oid": uuid.NAMESPACE_OID,
            "x500": uuid.NAMESPACE_X500,
        }
        try:
            ns = namespaces[uuid_namespace.lower()]
        except KeyError:
            raise click.ClickException("Invalid namespace, must be in {dns, url, oid, x500}")
    elif uuid_version in (3, 5):
        raise click.ClickException(f"Namespace must be provided for version {uuid_version}")

    if uuid_version == 1:
        value = str(uuid.uuid1())
    elif uuid_version == 3:
        value = str(uuid.uuid3(ns, uuid_name))
    elif uuid_version == 4:
        value = str(uuid.uuid4())
    elif uuid_version == 5:
        value = str(uuid.uuid5(ns, uuid_name))
    else:
        raise click.ClickException("Invalid version")

    if upper:
        value = value.upper()

    return value
