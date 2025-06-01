from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.registration_form_component = RegistrationFormComponent(page)
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_registration_form(self, email="user.name@gmail.com", username="username", password="password"):
        self.registration_form_component.fill(email, username, password)

    def check_visible(self):
        self.registration_form_component.check_visible()

    def click_registration_button(self):
        self.registration_button.click()









