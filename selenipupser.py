from selenium.common.exceptions import WebDriverException
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as match

driver: WebDriver = ...  # потрібна тільки заглушка, тому що драйвер створюємо в тесті - див. SDET A1+ Selenium 2.05.00


def visit(url):
    driver.get(url)


def wait():
    return WebDriverWait(driver, 4)


def by(css_selector: str):
    return By.CSS_SELECTOR, css_selector


def wait_visible(selector) -> WebElement:
    return wait().until(match.visibility_of_element_located(by(selector)))


def assert_text(locator, value):
    wait().until(match.text_to_be_present_in_element(locator, value))


def assert_value(locator, attribute_value):
    wait().until(match.text_to_be_present_in_element_value(locator, attribute_value))


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


class Element:
    def __init__(self, selector):
        self.selector = selector

    def assert_text(self, value):
        wait().until(match.text_to_be_present_in_element(by(self.selector), value))
        return self

    def assert_value(self, value):
        wait().until(match_value_of_element(by(self.selector), value))
        return self

    def type(self, keys):
        wait_visible(self.selector).send_keys(keys)
        return self

    def press_enter(self):
        wait_visible(self.selector).send_keys(Keys.ENTER)
        return self


def element(selector) -> Element:
    return Element(selector)
