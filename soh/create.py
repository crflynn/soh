"""File creation helper functionality.

Entry point: $ soh create gitignore [OPTS] <text>
Entry point: $ soh create license [OPTS] <text>
"""
import os

import click
import requests

from soh.util import clipboard_output
from soh.util import ensure_ok_response


GITIGNORE_FILE = ".gitignore"
LICENSE_FILE = "LICENSE.txt"


@click.group(invoke_without_command=False, short_help="+ Create files")
def create():
    """Create files."""
    pass  # pragma: no cover


@create.command(short_help="Create a .gitignore file from github.com/git/gitignore")
@click.option("-o", "--overwrite", is_flag=True, default=False, show_default=True, help="overwrite existing .gitignore")
@click.argument("language")
@clipboard_output
def gitignore(language, overwrite):
    """Create a .gitignore file.

    Use `list` to get a list of available languages.
    """
    response = requests.get("https://api.github.com/repos/github/gitignore/contents")
    ensure_ok_response(response, "Fetching .gitignore files failed.")

    contents = response.json()

    if language == "list":
        languages = []
        for element in contents:
            filename_split = element["name"].split(".")
            if filename_split[-1] == "gitignore":
                languages.append(filename_split[0].lower())
        return " * " + "\n * ".join(languages)

    download_url = None
    for element in contents:
        if language.lower() == element["name"].split(".")[0].lower():
            download_url = element["download_url"]

    if download_url is None:
        raise click.ClickException("Language " + language + " could not be found.")

    response = requests.get(download_url)
    ensure_ok_response(response, "Fetching .gitignore file failed.")

    file_exists = os.path.isfile(GITIGNORE_FILE)

    if file_exists and overwrite is False:
        raise click.ClickException(GITIGNORE_FILE + " file already exists. Delete it or use -o to overwrite.")

    with open(GITIGNORE_FILE, "w") as f:
        f.write(response.text)

    return "File " + GITIGNORE_FILE + " was created."


@create.command(name="license", short_help="Create a LICENSE.txt file from github.com/github/choosealicense.com")
@click.option("-o", "--overwrite", is_flag=True, default=False, show_default=True, help="overwrite existing .gitignore")
@click.argument("value")
@clipboard_output
def license_(value, overwrite):
    """Create a LICENSE.txt file.

    Use `list` to get a list of available licenses.
    """
    response = requests.get("https://api.github.com/repos/github/choosealicense.com/contents/_licenses?ref=gh-pages")
    ensure_ok_response(response, "Fetching license files failed.")

    contents = response.json()

    if value == "list":
        licenses = []
        for element in contents:
            filename_split = element["name"].split(".")
            if filename_split[-1] == "txt":
                licenses.append(filename_split[0].lower())
        return " * " + "\n * ".join(licenses)

    download_url = None
    for element in contents:
        if value.lower() == element["name"].split(".")[0].lower():
            download_url = element["download_url"]

    if download_url is None:
        raise click.ClickException("License " + value + " could not be found.")

    response = requests.get(download_url)
    ensure_ok_response(response, "Fetching LICENSE file failed.")

    file_exists = os.path.isfile(LICENSE_FILE)

    if file_exists and overwrite is False:
        raise click.ClickException(LICENSE_FILE + " file already exists. Delete it or use -o to overwrite.")

    with open(LICENSE_FILE, "w") as f:
        # files have metadata in header with --- separators
        f.write(response.text.split("---")[-1].strip())

    return "File " + LICENSE_FILE + " was created."
