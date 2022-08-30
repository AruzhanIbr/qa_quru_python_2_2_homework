
from selene.support.shared import browser
from selene import be, have
import pytest

#фикстуры в файле conftest
def test_negative():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selenide: User-oriented Web UI browser tests in Python'))


