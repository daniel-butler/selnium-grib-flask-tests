from flask import url_for
import pytest


@pytest.fixture
def selenium(selenium, live_server):
    yield selenium
    selenium.close()


def test_opening_up_web_page(selenium):
    # create the url per the pytest-selenium docs
    url = url_for('hi', _external=True)

    # go to the web page
    selenium.get(url)

    # print out the beginning of what is found
    print(selenium.page_source[:100])

    # test that the title is hello from the flask app
    assert selenium.title == 'Hello'

