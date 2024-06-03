from selene import browser, have, command
import os
import tests
from data.user import User


class RegistrationPage:
    def __init__(self):
        self._state = browser.element("#state")
        self._city = browser.element("#city")

    def open(self):
        browser.open("/automation-practice-form")
        return self

    def _fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    def _fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    def _fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    def _fill_gender(self, value):
        browser.all(".custom-control-label").element_by(have.exact_text(value)).click()
        return self

    def _fill_phone_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    def _fill_date_of_birth(self, year, month, day):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__month-select").type(month)
        browser.element(".react-datepicker__year-select").type(year)
        browser.element(
            f".react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)"
        ).click()
        return self

    def _fill_subjects(self, value):
        browser.element("#subjectsInput").type(value).press_tab()
        return self

    def _fill_hobbies(self, value):
        browser.all(".custom-control-label").element_by(have.exact_text(value)).click()
        return self

    def _upload_picture(self, path):
        browser.element("#uploadPicture").send_keys(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), "pictures/", path)
            )
        )
        return self

    def _fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    def _submit(self):
        browser.element("#submit").click()
        return self

    def _fill_state(self, value):
        self._state.perform(command.js.scroll_into_view)
        self._state.click()
        browser.all('[id^="react-select-3-option-"]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def _fill_city(self, value):
        self._city.perform(command.js.scroll_into_view)
        self._city.click()
        browser.all('[id^="react-select-4-option-"]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def register(self, student: User):
        (
            self._fill_first_name(student.name)
            ._fill_last_name(student.surname)
            ._fill_email(student.email)
            ._fill_gender(student.gender)
            ._fill_phone_number(student.phone)
            ._fill_date_of_birth(
                student.date_year, student.date_month, student.date_day
            )
            ._fill_subjects(student.subject)
            ._fill_hobbies(student.hobby)
            ._upload_picture(student.photo)
            ._fill_address(student.address)
            ._fill_state(student.state)
            ._fill_city(student.city)
            ._submit()
        )
        return self

    def should_registered_user_with(self, student: User):
        browser.element(".table").all("td").even.should(
            have.exact_texts(
                f"{student.name} {student.surname}",
                student.email,
                student.gender,
                student.phone,
                f"{student.date_day} {student.date_month},{student.date_year}",
                student.subject,
                student.hobby,
                student.photo,
                student.address,
                f"{student.state} {student.city}",
            )
        )
