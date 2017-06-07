import os

import pytest


def pytest_addoption(parser):
    parser.addini("env",
                  type="linelist",
                  help="a line separated list of environment variables of the form NAME=VALUE)",
                  default=[])


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    for e in early_config.getini("env"):
        part = e.partition("=")
        key = part[0].strip()
        value = part[2].strip()

        # use D: as a way to designate a default value 
        # that will only override env variables if they 
        # do not exist already
        dkey = key.split("D:")
        default_val = False
        if len(dkey) == 2:
            key = dkey[1]
            default_val = True

        if not default_val or key not in os.environ:
            os.environ[key] = value
