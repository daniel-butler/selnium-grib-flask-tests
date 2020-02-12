import pytest


@pytest.fixture
def selenium(selenium):
    yield selenium
    selenium.close()


def test_opening_up_web_page(selenium):
    # go to the web page
    url = 'http://0.0.0.0:5000'
    print(url)
    selenium.get(url)

    # print out the beginning of what is found
    print(selenium.page_source[:100])

    # test that the title is hello from the flask app
    assert selenium.title == 'Hello'

