soh (sleight-of-hand)
=====================

|travis| |codecov| |pypi| |pyversions|


.. |travis| image:: https://img.shields.io/travis/crflynn/soh.svg
    :target: https://travis-ci.org/crflynn/soh

.. |codecov| image:: https://codecov.io/gh/crflynn/soh/branch/master/graphs/badge.svg
    :target: https://codecov.io/gh/crflynn/soh

.. |pypi| image:: https://img.shields.io/pypi/v/soh.svg
    :target: https://pypi.python.org/pypi/soh

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/soh.svg
    :target: https://pypi.python.org/pypi/soh

Sleight of hand, or ``soh``, is a command line tool that handles a lot of common tasks for developers. For the most part, it offers a convenient command line interface to a lot of standard library operations, such as base64 encoding, creating datetime strings, fetching system information, uuid generation, etc.


Installation
------------

To install ``soh`` use ``pip``.

.. code-block:: shell

    pip install soh



Usage
-----

The entry point for all commands is

.. code-block:: shell

    $ soh
    Usage: soh [OPTIONS] COMMAND [ARGS]...

      Sleight of hand CLI commands.

      (+) indicates command group. Use the -c flag on most commands to copy
      output to clipboard

    Options:
      -h, --help  Show this message and exit.

    Commands:
      b64      + Base64 operations
      create   + Create files
      dt       + Datetimes
      epoch    + Epoch times
      json     JSON printing
      jwt      Display JWT contents
      secret   + Secrets generators
      serve    Simple http server at current directory
      sys      + System information
      uuid     Generate UUIDs
      version  soh CLI version



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


``pre-commit`` will enforce ``black`` code formatting to pass before committing. The configuration for ``black`` is in the ``pyproject.toml`` file.

To run tests,

.. code-block:: shell

    pytest


The testing configuration is found in ``pytest.ini``.