from selene import browser, be, have


def test_form_autocomplete():
    browser.open('/')
    browser.element('#firstName').should(be.blank).type('Artem')
    browser.element('#lastName').should(be.blank).type('Ilichev')
    browser.element('#userEmail').should(be.blank).type('test@mail.ru')
    browser.all('#genterWrapper>div>div').should(have.exact_texts('Male', 'Female', 'Other'))
    browser.all('.col-md-9.col-sm-12>div').element_by(have.exact_text('Other')).click()
    browser.element('#userNumber').type('90957485747')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select>option').element_by(have.exact_text('1989')).click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select>option').element_by(have.exact_text('March')).click()
    browser.element('.react-datepicker__day.react-datepicker__day--021').click()
    browser.element('.css-2b097c-container').click()




