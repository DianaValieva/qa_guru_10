from data.users import User
from pages.reg_page import RegistrationPage


def test_registration_successful():
    user = User(
        first_name='Diana',
        last_name='Valieva',
        user_email='di7051@gmail.com',
        user_gender='Female',
        user_phone_number='9874956293',
        month='December',
        year='1991',
        day='30',
        user_subject='Maths',
        user_hobby='Sports',
        user_picture='dog.jpg',
        user_current_address='Ufa',
        user_state='NCR',
        user_city='Delhi',
    )

    reg_page = RegistrationPage()
    reg_page.open_registration_page()
    reg_page.register(user)
    reg_page.check_registration(user)
