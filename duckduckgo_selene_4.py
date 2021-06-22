from selene import be, have
from selene.support.shared import browser


# def test_duck_selene():
#
#     browser.open('https://duckduckgo.com/')
#
#     browser.wait_visible('[name=q]') \
#         .should(be.blank) \
#         .type('yashaka selene python').press_enter()
#     browser.all('.result__body') \
#         .should(have.size_greater_than(5)) \
#         .first.should(have.text('User-oriented Web UI browser tests'))
#
#     browser.all('.result__body').first.wait_visible('a').click()
#     browser.should(have.title_containing('yashaka/selene'))

#############
from selene.support.shared.jquery_style import s
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as match
from webdriver_manager.chrome import ChromeDriverManager


class match_value_of_element(object):
    """
    An expectation for checking if the given text is present in the element's
    locator, text
    """
    def __init__(self, locator, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            value = driver.find_element(*self.locator).get_attribute("value")
            return self.text == value

        except WebDriverException:
                return False

def by(css_selector: str):
    return (By.CSS_SELECTOR, css_selector)


def element(selector) -> WebElement:
    return wait.until(match.visibility_of_element_located(by(selector)))


def assert_text(locator, value):
    wait.until(match.text_to_be_present_in_element(locator, value))


def assert_value(locator, attribute_value):
    wait.until(match.text_to_be_present_in_element_value(locator, attribute_value))


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
wait = WebDriverWait(driver, 4)

browser.config.driver = driver  # для того, щоб оригінальний код з селеном (внизу) юзав selenium_WebDriver замість свого

# browser.open('https://duckduckgo.com/')
driver.get('https://duckduckgo.com/')


class Element:
    def __init__(self, selector):
        self.selector = selector

    def assert_text(self, value):
        wait.until(match.text_to_be_present_in_element(by(self.selector), value))
        return self

    def assert_value(self, attribute_value):
        wait.until(match_value_of_element(by(self.selector), attribute_value))
        return self

    def type(self, keys:str):
        element(self.selector).send_keys(keys)
        return self

    def press_enter(self):
        element(self.selector).send_keys(Keys.ENTER)
        return self


# query = '[name=q]'
# assert_text(by(query), '')
# assert_value(by(query), '')
# element(query).send_keys('yashaka selene python' + Keys.ENTER)


Element('[name=q]')\
    .assert_text('').assert_value('')\
    .type('yashaka selene python')\
    .press_enter()


# browser.element('[name=q]')\
#     .should(have.exact_text('').and_(have.value('')))\
#     .type('yashaka selene python').press_enter()
#
#
# browser.all('.result__body') \
#     .should(have.size_greater_than(5)) \
#     .first.should(have.text('User-oriented Web UI browser'))
#
# browser.all('.result__body').first.element('a').click()
# browser.should(have.title_containing('yashaka/selene'))