from selene import have
from selene.support.shared import browser


class Panel:
    def __init__(self):
        self.container = browser.element('.left-pannel')

    def open(self, item):
        browser.open('/elements')
        self.container.all('li').element_by(have.exact_text(item)).click()

    def open_simple_registration_form(self):
        self.open('Text Box')