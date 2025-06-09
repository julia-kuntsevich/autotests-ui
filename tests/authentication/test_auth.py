import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
        registration_page.registration_form_component.fill(email="user.name@gmail.com", username="username", password="password")
        registration_page.click_registration_button()

        registration_page.page.wait_for_timeout(2000)

        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar_component.check_visible("username")
        dashboard_page.sidebar_component.check_visible()
        dashboard_page.sidebar_component.click_logout()

        login_page.login_form_component.fill(email="user.name@gmail.com", password="password")
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar_component.check_visible("username")
        dashboard_page.sidebar_component.check_visible()

    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.login_form_component.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
        login_page.click_registration_link()

        registration_page.registration_form_component.check_visible(email="", username="", password="")
