from playwright.sync_api import Page

from pages.base_page import BasePage
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
import re

class RegistrationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.registration_form_component = RegistrationFormComponent(page)
        self.registration_button = Button(page,'registration-page-registration-button', 'Reg_Button')
        self.login_link = Link(page, 'registration-page-login-link','Login')

    def click_login_link(self):
        self.login_link.click()
        # Добавили проверку
        self.check_current_url(re.compile(".*/#/auth/login"))

    def fill_registration_form(self, email="user.name@gmail.com", username="username", password="password"):
        self.registration_form_component.fill(email, username, password)

    def check_visible(self):
        self.registration_form_component.check_visible()

    def click_registration_button(self):
        self.registration_button.click()










