from selene import be, have
from selene.support.shared import browser

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import ChromeOptions

import selenipupser

from selenipupser import element, visit

def test_duck_upser():

    options = ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

    selenipupser.driver = driver

    visit('https://duckduckgo.com/')

    element('[name=q]')\
        .assert_text('').assert_value('')\
        .type('yashaka selene python').press_enter()


# selenipupser code above
# =======================
# selene code below commented as a goal to reach
# ----------------------------------------------
# browser.config.driver = driver
# browser.all('.result__body') \
#     .should(have.size_greater_than(5)) \
#     .first.should(have.text('User-oriented Web UI browser tests'))
#
# browser.all('.result__body').first.element('a').click()
# browser.should(have.title_containing('yashaka/selene'))
# ----------------------------------------------
# selenium code below to refactor
# ===============================





# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as match
# from selenium.webdriver.common.by import By
# wait = WebDriverWait(driver, 4)
#
# results = driver.find_elements(By.CSS_SELECTOR, '.result__body')
# assert len(results) > 5
# assert 'User-oriented Web UI browser tests' in results[0].text
#
# results[0].find_element(By.CSS_SELECTOR, 'a').click()
# wait.until(match.title_contains('yashaka/selene'))
#
# driver.quit()
