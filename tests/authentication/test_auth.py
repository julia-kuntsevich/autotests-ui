import allure
import pytest
from tools.routes import AppRoute
from config import settings
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.login_page import LoginPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.AUTHORIZATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.AUTHORIZATION)
class TestAuthorization:
    @allure.title("User login with correct email and password")
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            dashboard_page: DashboardPage,
            registration_page: RegistrationPage
    ):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form_component.fill(email=settings.test_user.email, username=settings.test_user.username, password=settings.test_user.password)
        registration_page.click_registration_button()

        registration_page.page.wait_for_timeout(2000)

        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar_component.check_visible("username")
        dashboard_page.sidebar_component.check_visible()
        dashboard_page.sidebar_component.click_logout()

        login_page.login_form_component.fill(email=settings.test_user.email, password=settings.test_user.password)
        login_page.click_login_button()

        # Проверка элементов Dashboard после входа
        dashboard_page.dashboard_toolbar_view_component.check_visible()
        dashboard_page.navbar_component.check_visible("username")
        dashboard_page.sidebar_component.check_visible()

    @pytest.mark.parametrize(
        "email, password",
        [
            ("user.name@gmail.com", "password"),
            ("user.name@gmail.com", "  "),
            ("  ", "password")
        ]
    )
    @allure.title("User login with wrong email or password")
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        login_page.visit(AppRoute.LOGIN)
        login_page.login_form_component.fill(email=email, password=password)
        login_page.click_login_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title("Navigation from login page to registration page")
    def test_navigate_from_authorization_to_registration(
            self,
            login_page: LoginPage,
            registration_page: RegistrationPage
    ):
        login_page.visit(AppRoute.LOGIN)
        login_page.click_registration_link()

        registration_page.registration_form_component.check_visible(email="", username="", password="")
