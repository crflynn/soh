soh (sleight-of-hand)
=====================

Sleight of hand, or ``soh``, is a command line tool that handles a lot of common tasks for developers. For the most part, it offers a convenient command line interface to a lot of standard library operations, such as base64 encoding, creating datetime strings, fetching system information, uuid generation, etc.


Installation
------------

Currently, ``soh`` can be installed using ``pip``. In the future, I hope to have it available in brew tap to be installed using ``brew``. To install use:

.. code-block:: shell

    pip install soh


Usage
-----

The entry point for all commands is

.. code-block:: shell

    $ soh


To get help on any command use the ``-h`` or ``--help`` flag.


.. code-block:: shell

    $ soh uuid -h
    Usage: soh uuid [OPTIONS]

      Generate UUIDs.

    Options:
      -v, --version INTEGER  uuid version  [default: 4]
      -ns, --namespace TEXT  namespace (v3, v5) {dns, url, oid, x500}
      -n, --name TEXT        name (v3, v5)
      -u, --upper            use upper case
      -c, --clip             copy to clipboard
      -h, --help             Show this message and exit.


To copy the execution output of most commands to clipboard, use the ``-c`` or ``--clip`` command.

.. code-block:: shell

    $ soh uuid -c
    c64af300-8895-4dff-b005-15dcd4c72f24 (copied to clipboard 📋)



Developer Setup
---------------

To set up a local development environment follow these (or portions of these) steps.

.. code-block:: shell

    # clone
    git clone git@github.com:crflynn/soh.git
    cd soh

    # setup pre-commit
    brew install pre-commit
    pre-commit install

    # setup pyenv and python 3
    brew install pyenv
    pyenv install 3.7.3
    pyenv local 3.7.3

    # setup poetry and install deps
    curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
    poetry install
    poetry install --develop soh
