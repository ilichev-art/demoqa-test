from demoqa_test.registration_page import RegistrationPage


def test_form_autocomplete():
    registration_page = RegistrationPage()
    registration_page.open()
    (
        registration_page.fill_first_name("Mahatma")
        .fill_second_name("Gandhi")
        .fill_email("test@mail.ru")
        .fill_gender("Other")
        .fill_phone("9095748574")
        .fill_date_of_birth("1989", "March", "21")
        .fill_subject("computer")
        .fill_hobbies("Sports")
        .upload_file("1703075063565.jpeg")
        .fill_current_address("Mytishchi")
        .fill_state_and_city("Haryana", "Karnal")
        .submit()
        .registered_user_with(
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

    # registration_page.open()
    #
    # # WHEN
    # registration_page.fill_first_name('Mahatma')
    # registration_page.fill_second_name('Gandhi')
    #
    # registration_page.fill_email('test@mail.ru')
    #
    # registration_page.fill_gender('Other')
    #
    # registration_page.fill_phone('9095748574')
    #
    # registration_page.fill_date_of_birth('1989', 'March', '21')
    #
    # registration_page.fill_subject('computer')
    #
    # registration_page.set_hobbies('Sports')
    #
    # registration_page.upload_file('1703075063565.jpeg')
    #
    # registration_page.fill_current_address('Mytishchi')
    #
    # registration_page.fill_state_and_city('Haryana', 'Karnal')
    #
    # registration_page.submit()
    #
    # #THEN
    # # Проверка введенных данных
    # registration_page.registered_user_with(
    #     'Mahatma Gandhi',
    #     'test@mail.ru',
    #     'Other',
    #     '9095748574',
    #     '21 March,1989',
    #     'Computer Science',
    #     'Sports',
    #     '1703075063565.jpeg',
    #     'Mytishchi',
    #     'Haryana Karnal'
    # )
