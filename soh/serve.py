"""Simple HTTP fileserver.

Entry point: $ soh serve [OPTS]
"""
from http.server import SimpleHTTPRequestHandler
import socketserver

import click


# TODO consider specifying the path


@click.command(short_help="Simple http server at current directory")
@click.option("-p", "--port", default=8080, show_default=True, help="port")
def serve(port):
    """Simple HTTP Server."""
    with socketserver.TCPServer(("", port), SimpleHTTPRequestHandler) as httpd:
        print("Serving at http://localhost:" + str(port) + " ... Press CTRL-C to quit.")
        httpd.serve_forever()
