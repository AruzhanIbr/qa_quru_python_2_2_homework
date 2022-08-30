from selene.support.shared import browser
from selene import be, have


# фикстуры в файле conftest
def test_first():
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(
        have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
