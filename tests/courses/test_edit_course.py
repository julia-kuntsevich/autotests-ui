import pytest
from fixtures.pages import courses_list_page
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
class TestCourses:
    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_form_component.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.image_upload_widget_component.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget_component.check_visible(is_image_uploaded=True)
        create_course_page.create_course_toolbar_view_component.click_button()
        courses_list_page.course_view_component.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )
        courses_list_page.courses_view_menu_component.click_edit(0)
        courses_list_page.edit_course_form_component.fill(
            title="Selenium",
            estimated_time="1 weeks",
            description="Selenium",
            max_score="20",
            min_score="2"
        )
        courses_list_page.edit_course_form_component.check_visible(
            title="Selenium",
            estimated_time="1 weeks",
            description="Selenium",
            max_score="20",
            min_score="2"
        )
        courses_list_page.edit_course_form_component.click_button()

