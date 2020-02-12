import pytest

from . import http_app


@pytest.fixture
def app():
    app = http_app.app
    return app

