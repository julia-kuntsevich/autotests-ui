from playwright.sync_api import sync_playwright, expect
from config import settings

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    # with page.expect_navigation():
    #  page.click('button:has-text("Registration")')
    #
    # dashboard_toolbar_title = page.get_by_test_id('dashboard-toolbar-title-text')
    # title_text = dashboard_toolbar_title.text_content()
    # expected_title = "Dashboard"
    #
    # if expected_title == title_text:
    #  print("Есть заголовок - Dashboard")
    # else:
    #  print("Заголовок отсутствует")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text('Dashboard')
