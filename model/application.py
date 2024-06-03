from model.components.panel import Panel
from model.demoqa_test.simple_registration_page import (
    SimpleRegistrationPage,
)


class Application:
    def __init__(self):
        self.simple_registration = SimpleRegistrationPage()
        self.panel = Panel()


app = Application()