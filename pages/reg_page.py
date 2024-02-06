from selene import browser, be, by, have
from pathlib import Path


class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        return self

    def fill_first_name(self, name):
        browser.element('#firstName').should(be.blank).type(name)
        return self

    def fill_last_name(self, name):
        browser.element('#lastName').should(be.blank).type(name)
        return self

    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)
        return self

    def fill_phone_number(self, num):
        browser.element('#userNumber').should(be.blank).type(num)
        return self

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_gender(self, sex):
        if sex == "Male":
            browser.element("#gender-radio-1").double_click()
        elif sex == 'Female':
            browser.element("#gender-radio-2").double_click()
        else:
            browser.element("#gender-radio-3").double_click()

    def fill_address(self, address):
        browser.element('#currentAddress').should(be.blank).type(address)
        return self

    def select_user_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()
        return self

    def user_hobby_checkbox(self, value):
        if value == "Sports":
            browser.element("[for='hobbies-checkbox-1']").click()
        elif value == "Reading":
            browser.element("[for='hobbies-checkbox-2']").click()
        elif value == "Music":
            browser.element("[for='hobbies-checkbox-3']").click()
        return self

    def user_picture(self, picture_name):
        pic_path= str(Path(__file__).parent.joinpath(f'resources/{picture_name}'))
        browser.element('#uploadPicture').send_keys(pic_path)
        return self

    def user_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def user_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit_the_form(self):
        browser.element('#submit').press_enter()
        return self

    def check_form(self,
                   full_name,
                   email,
                   gender,
                   number,
                   date_of_birth,
                   subjects,
                   hobbies,
                   file,
                   current_address,
                   state_and_city,):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                file,
                current_address,
                state_and_city,
            )
        )
        return self


