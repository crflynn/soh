soh (sleight-of-hand)
=====================

Setup
-----

.. code-block:: shell

    # clone
    git clone git@github.com:crflynn/soh.git
    cd soh
    # setup pre-commit (black)
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
