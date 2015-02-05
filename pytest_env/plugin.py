import os


def pytest_addoption(parser):
    parser.addini("env",
                  type="linelist",
                  help="a line separated list of environment variables of the form NAME=VALUE)",
                  default=[])


def pytest_load_initial_conftests(args, early_config, parser):
    for e in early_config.getini("env"):
        part = e.partition("=")
        key = part[0].strip()
        value = part[2].strip()
        os.environ[key] = value