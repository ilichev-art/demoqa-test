from selene import browser
from data.users import User


class SimpleRegistrationPage:
    def __init__(self):
        self.full_name = browser.element('#userName')
        self.email = browser.element('#userEmail')
        self.currentAddress = browser.element('#currentAddress')
        self.permanentAddress = browser.element('#permanentAddress')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/text-box')
        return self

    def fill_full_name(self, value):
        self.full_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def fill_current_address(self, value):
        self.currentAddress.type(value)

    def fill_permanent_address(self, value):
        self.permanentAddress.type(value)

    def submit(self):
        self.submit_button.click()

    def register(self, user: User):
        self.fill_full_name(user.full_name)
        self.fill_email(user.email)
        self.fill_current_address(user.address)
        self.fill_permanent_address(user.permanent_address)
        self.submit()
        return self