from data.user import User
from demoqa_test.pages import RegistrationPage


def test_user_can_send_form():
    page = RegistrationPage()
    user = User('Mahatma',
                'Gandhi',
                'test@mail.ru',
                'Other',
                '9095748574',
                '1989', 'March', '21',
                'Computer Science',
                'Sports',
                '1703075063565.jpeg',
                'Mytishchi',
                'Haryana',
                'Karnal'
                )
    page.open().register(user).should_registered_user_with(user)