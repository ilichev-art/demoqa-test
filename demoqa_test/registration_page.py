from pathlib import Path

from selene import browser, have, command

import tests


class RegistrationPage:
    def __init__(self):
        self.state = browser.element("#state")
        self.city = browser.element("#city")

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def fill_second_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def fill_gender(self, value):
        browser.all("[name=gender]").element_by(have.value(value)).element("..").click()
        return self

    def fill_phone(self, value):
        browser.element("#userNumber").type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").click()
        browser.all(".react-datepicker__year-select>option").element_by(
            have.exact_text(year)
        ).click()
        browser.element(".react-datepicker__month-select").click()
        browser.all(".react-datepicker__month-select>option").element_by(
            have.exact_text(month)
        ).click()
        browser.element(f".react-datepicker__day.react-datepicker__day--0{day}").click()
        return self

    def fill_subject(self, value):
        browser.element("#subjectsInput").type(value).press_tab()
        return self

    def upload_file(self, file_name):
        browser.element("#uploadPicture").set_value(
            str(
                Path(tests.__file__).parent.joinpath(f"pictures/{file_name}").absolute()
            )
        )
        return self

    def fill_hobbies(self, value):
        browser.all(".custom-checkbox").element_by(have.exact_text(value)).click()
        return self

    def fill_current_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def fill_state_and_city(self, state, city):
        self.state.perform(command.js.scroll_into_view)
        self.state.click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(state)
        ).click()
        self.city.perform(command.js.scroll_into_view)
        self.city.click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text(city)
        ).click()
        return self

    def submit(self):
        browser.element("#submit").click()
        return self

    def registered_user_with(self, full_name, email, gender, phone, date_of_birth, subject, hobby, photo, address, state):
        browser.element(".modal-content").element("table").all("tr").all(
            "td"
        ).even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subject,
                hobby,
                photo,
                address,
                state,
            )
        )
