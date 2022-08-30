from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    browser.config.window_height = 458
    browser.config.window_width = 998
    browser.open('https://google.com')
    yield
    browser.close()
