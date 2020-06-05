import pytest

from . import http_app


@pytest.fixture
def app():
    return http_app.app

