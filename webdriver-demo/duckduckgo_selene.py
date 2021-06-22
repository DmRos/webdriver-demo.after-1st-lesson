from selene import be, have
from selene.support.shared import browser

browser.open('https://duckduckgo.com/')

browser.element('[name=q]') \
    .should(be.blank) \
    .type('yashaka selene python').press_enter()
browser.all('.result__body') \
    .should(have.size_greater_than(5)) \
    .first.should(have.text('User-oriented Web UI browser tests'))

browser.all('.result__body').first.element('a').click()
browser.should(have.title_containing('yashaka/selene'))
