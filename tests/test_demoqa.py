from pathlib import Path
import allure
from selene import browser, have, command

import tests


def test_form_autocomplete(setup_browser):
    with allure.step("Open site"):
        browser.open("/automation-practice-form")

    with allure.step("Fill form"):
        browser.element("#firstName").type("Mahatma")
        browser.element("#lastName").type("Gandhi")
        browser.element("#userEmail").type("test@mail.ru")
        browser.element("#genterWrapper").element('[for="gender-radio-3"]').click()
        browser.element("#userNumber").type("9095748574")
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").click()
        browser.all(".react-datepicker__year-select>option").element_by(
            have.exact_text("1989")
        ).click()
        browser.element(".react-datepicker__month-select").click()
        browser.all(".react-datepicker__month-select>option").element_by(
            have.exact_text("March")
        ).click()
        browser.element(".react-datepicker__day.react-datepicker__day--021").click()
        browser.element("#subjectsInput").type("computer").press_tab()
        browser.element('[for="hobbies-checkbox-1"]').click()
        # browser.element('#uploadPicture').send_keys(os.path.abspath('pictures/1703075063565.jpeg'))
        browser.element("#uploadPicture").set_value(
            str(
                Path(__file__)
                .parent.joinpath(f"pictures/1703075063565.jpeg")
                .absolute()
            )
        )
        browser.element("#currentAddress").type("Mytishchi")
        browser.element("#state").perform(command.js.scroll_into_view)
        browser.element("#state").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text('Haryana')
        ).click()
        browser.element("#city").perform(command.js.scroll_into_view)
        browser.element("#city").click()
        browser.all("[id^=react-select][id*=option]").element_by(
            have.exact_text('Karnal')
        ).click()

    with allure.step("Submit form"):
        browser.element("#submit").click()

    with allure.step("Checking data"):
        browser.element(".modal-content").element("table").all("tr").all(
            "td"
        ).even.should(
            have.exact_texts(
                (
                    "Mahatma Gandhi",
                    "test@mail.ru",
                    "Other",
                    "9095748574",
                    "21 March,1989",
                    "Computer Science",
                    "Sports",
                    "1703075063565.jpeg",
                    "Mytishchi",
                    "Haryana Karnal",
                )
            )
        )
