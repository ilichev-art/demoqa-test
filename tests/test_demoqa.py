from selene import browser, be, have
import os


def test_form_autocomplete():
    browser.open('/')
    # Ввод данных
    browser.element('#firstName').should(be.blank).type('Mahatma')
    browser.element('#lastName').should(be.blank).type('Gandhi')
    browser.element('#userEmail').should(be.blank).type('test@mail.ru')
    browser.all('#genterWrapper>div>div').should(have.exact_texts('Male', 'Female', 'Other'))
    browser.all('.col-md-9.col-sm-12>div').element_by(have.exact_text('Other')).click()
    browser.element('#userNumber').type('9095748574')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select>option').element_by(have.exact_text('1989')).click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select>option').element_by(have.exact_text('March')).click()
    browser.element('.react-datepicker__day.react-datepicker__day--021').click()
    browser.element('#subjectsInput').should(be.clickable).type('computer').press_tab()
    browser.all('#hobbiesWrapper>div>div').should(have.exact_texts('Sports', 'Reading', 'Music'))
    browser.element('.custom-control.custom-checkbox.custom-control-inline').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('/Users/a.ilichev/Downloads/1703075063565.jpeg'))
    browser.element('#currentAddress').should(be.blank).type('Mytishchi')
    browser.element('#state').click()
    browser.element('#state [class$=menu] [id$=option-2]').should(have.text('Haryana')).click()
    browser.element('#city').click()
    browser.element('#city [class$=menu] [id$=option-0]').should(have.exact_text('Karnal')).click()
    browser.element('#submit').should(be.clickable).click()

    # Проверка введенных данных
    browser.element(('css selector', '.modal-content')).element(('css selector', 'table')).all(
        ('css selector', 'tr')).all(('css selector', 'td'))[1::2].should(
        have.exact_texts(
            'Mahatma Gandhi',
            'test@mail.ru',
            'Other',
            '9095748574',
            '21 March,1989',
            'Computer Science',
            'Sports',
            '1703075063565.jpeg',
            'Mytishchi',
            'Haryana Karnal'
        ))




