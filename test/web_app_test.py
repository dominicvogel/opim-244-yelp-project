# this is the "test/web_app_test.py" file...

# testing a flask app. see:
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/flask.md#testing
# ... https://flask.palletsprojects.com/en/2.1.x/testing/

import pytest
from bs4 import BeautifulSoup

from web_app import create_app


@pytest.fixture(scope="module")
def test_client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()


def test_home(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Welcome to our Georgetown Yelp Application</h1>" in response.data


def test_about(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>About this project</h1>" in response.data

def test_search(test_client):
    #
    # DEFAULT SYMBOL
    #
    response = test_client.get("/input/form")
    assert response.status_code == 200
    assert b"<h2>Term (pizza)</h2>" in response.data
    assert b"<h2>Location (georgetown)</h2>" in response.data
    assert b"Late Night Food Options" in response.data

    #
    # CUSTOMIZED SYMBOL VIA URL PARAMS
    #
    #response = test_client.get("/input/form")
    #assert response.status_code == 200
    #assert b"<h2>Stocks Dashboard (GOOGL)</h2>" in response.data
    #assert b"Latest Close: " in response.data