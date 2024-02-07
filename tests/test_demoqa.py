from pages.reg_page import RegistrationPage


def test_registration_successful():
    reg_page = RegistrationPage()
    reg_page.open()

    reg_page.fill_first_name("Diana")
    reg_page.fill_last_name("Valieva")
    reg_page.fill_email("di7051@gmail.com")
    reg_page.fill_phone_number("9874956293")
    reg_page.fill_date_of_birth("30", "December", "1991")
    reg_page.fill_gender("Female")
    reg_page.select_user_subject("Maths")
    reg_page.user_hobby_checkbox("Sports")
    reg_page.user_picture("dog.jpg")
    reg_page.fill_address("Ufa")
    reg_page.user_state("NCR")
    reg_page.user_city("Delhi")

    reg_page.submit_the_form()
    reg_page.check_form("Diana Valieva", 'di7051@gmail.com', 'Female', '9874956293', '30 December,1991', "Maths",
                        "Sports", "dog.jpg", "Ufa", 'NCR Delhi')
