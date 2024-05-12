from selene import browser, have
import os


def test_form_autocomplete():

    # Открытие раздела с формой ввода данных
    browser.open('/automation-practice-form')

    # Ввод данных
    # Ввод FistName и LastName
    browser.element('#firstName').type('Mahatma')
    browser.element('#lastName').type('Gandhi')

    # Ввод почты
    browser.element('#userEmail').type('test@mail.ru')

    # Активация радиокнопки в блоке Gender
    browser.element('#genterWrapper').element('[for="gender-radio-3"]').click()

    # Ввод номера телефона
    browser.element('#userNumber').type('9095748574')

    # Установка даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.all('.react-datepicker__year-select>option').element_by(have.exact_text('1989')).click()
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select>option').element_by(have.exact_text('March')).click()
    browser.element('.react-datepicker__day.react-datepicker__day--021').click()
    # Выбор предмета
    browser.element('#subjectsInput').type('computer').press_tab()

    # Активация чек-бокса в разделе Hobbies
    browser.element('[for="hobbies-checkbox-1"]').click()

    # Загрузка изображения
    browser.element('#uploadPicture').send_keys(os.path.abspath('Pictures/1703075063565.jpeg'))

    # Ввод адреса
    browser.element('#currentAddress').type('Mytishchi')

    # Выбор штата и города
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()

    # Отправка данных
    browser.element('#submit').click()

    # Проверка введенных данных
    browser.element('.modal-content').element('table').all(
        'tr').all('td').even.should(have.exact_texts((
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
        )))



