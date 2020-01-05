# soh (sleight-of-hand)

Sleight of hand, or `soh`, is a command line tool that handles a lot of common tasks for developers. For the most part, it offers a convenient command line interface to a lot of standard library operations, such as base64 encoding, creating datetime strings, fetching system information, uuid generation, etc.


## Installation

To install `soh`... TODO

You can also install using [homebrew](https://brew.sh/). To install use the command:

```
brew install crflynn/formula/soh
```

## Usage

The entry point for all commands is

```bash
$ soh
soh (sleight-of-hand) 0.1.0
Sleight of hand CLI commands.

    (+) indicates command group. Use the -c flag on most commands to copy
    output to clipboard

USAGE:
    soh [SUBCOMMAND]

FLAGS:
    -h, --help       Prints help information
    -V, --version    Prints version information

SUBCOMMANDS:
    help       Prints this message or the help of the given subcommand(s)
    uuid       Generate UUIDs
    version    Show soh version
```

To get help on any command use the ``-h`` or ``--help`` flag.


```bash
$ soh uuid -h
soh-uuid
Generate UUIDs

USAGE:
    soh uuid [FLAGS] [OPTIONS]

FLAGS:
    -c, --clip       Copy output to clipboard
    -h, --help       Prints help information
    -u, --upper      To upper case
    -V, --version    Prints version information

OPTIONS:
    -n <name>             UUID v3/5 name
    -s <namespace>        UUID v3/5 namespace (dns, oid, url, or x500)
    -v <version>          UUID version
```

To copy the execution output of most commands to clipboard, use the `-c` or `--clip` command.

```bash
$ soh uuid -c
c64af300-8895-4dff-b005-15dcd4c72f24 (copied to clipboard 📋)
```