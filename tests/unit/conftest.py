import sys

from mock import MagicMock
from os import path

import pytest


def pytest_configure(config):
    """
    Initial test env setup
    """
    sys.path.append(path.join("backend", "lambda_layers", "boto_utils", "python"))
    sys.path.append(path.join("backend", "lambda_layers", "cr_helper", "python"))
    sys.path.append(path.join("backend", "lambda_layers", "decorators", "python"))
    sys.path.append(path.join("backend", "lambdas", "jobs"))


@pytest.fixture(autouse=True)
def decorator_mocks(monkeypatch):
    """
    Mock the logging and tracing decorators
    """

    def mock_decorator(func):
        return func

    import decorators
    monkeypatch.setattr(decorators, "with_logger", mock_decorator)


@pytest.fixture(autouse=True)
def cr_helper_mocks(monkeypatch):
    """
    Mock the Custom Resource Helper
    """

    import crhelper
    monkeypatch.setattr(crhelper, "CfnResource", MagicMock())
