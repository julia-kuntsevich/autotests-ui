from playwright.sync_api import expect, Page
import pytest

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state : Page):
    page = chromium_page_with_state

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_button = page.locator('//div/h6[@data-testid = "courses-list-toolbar-title-text"]')
    expect(courses_button).to_be_visible()
    expect(courses_button).to_have_text('Courses')

    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    no_results = page.locator('//div/h6[@data-testid="courses-list-empty-view-title-text"]')
    expect(no_results).to_be_visible()
    expect(no_results).to_have_text('There is no results')
