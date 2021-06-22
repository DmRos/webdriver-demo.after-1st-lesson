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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as match
from webdriver_manager.chrome import ChromeDriverManager


def by(css_selector: str):
    return (By.CSS_SELECTOR, css_selector)


driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
browser.config.driver = driver # для того, щоб оригінальний код з селеном (внизу) юзав selenium_WebDriver замість свого

# def test_duck_ene():

# browser.open('https://duckduckgo.com/')
driver.get('https://duckduckgo.com/')
wait = WebDriverWait(driver, 4)
element = wait.until(match.visibility_of_element_located(by('[name=q]')))

# element = driver.find_element_by_css_selector('[name=q]')
# assert element.text == ''
wait.until(match.text_to_be_present_in_element(by('[name=q]'), ''))
assert element.get_attribute('value') == ''
# wait.until(match.text_to_be_present_in_element_value(by('[name=q]'), ''))


s('[name=q]').should(have.exact_text('').and_(have.value('')))

browser.element('[name=q]')\
    .should(be.blank)\
    .type('yashaka selene python').press_enter()
browser.all('.result__body') \
    .should(have.size_greater_than(5)) \
    .first.should(have.text('User-oriented Web UI browser'))

browser.all('.result__body').first.element('a').click()
browser.should(have.title_containing('yashaka/selene'))