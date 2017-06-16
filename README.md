# pytest-env

This is a py.test plugin that enables you to set environment variables in the pytest.ini file.

## Installation

Install with pip:

    pip install pytest-env

Uninstall with pip:

    pip uninstall pytest-env

## Usage

In your pytest.ini file add a key value pair with `env` as the key and the environment variables as a line separated list of `KEY=VALUE` entries.  The defined variables will be added to the environment before any tests are run:

    [pytest]
    env =
        HOME=~/tmp
        RUN_ENV=test

You can use `D:` (default) as prefix if you don't want to override existing environment variables:

    [pytest]
    env =
        D:HOME=~/tmp
        D:RUN_ENV=test

Lastly, you can use existing environment variables using a python-like format:

    [pytest]
    env =
        RUN_PATH=/run/path/{USER}
