import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
        courses_list_page.navbar_component.check_visible('username')
        courses_list_page.sidebar_component.check_visible()
        courses_list_page.toolbar_view_component.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")
        create_course_page.create_course_toolbar_view_component.check_visible_title()
        create_course_page.image_upload_widget_component.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form_component.check_visible(
            title="", estimated_time="", description="", max_score="0", min_score="0"
        )

        create_course_page.create_course_exercises_toolbar_view_component.check_visible_title()
        create_course_page.check_visible_exercises_empty_view()

        create_course_page.image_upload_widget_component.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget_component.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form_component.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.create_course_toolbar_view_component.click_button()

        courses_list_page.toolbar_view_component.check_visible()
        courses_list_page.course_view_component.check_visible(
            index=0,
            title="Playwright",
            max_score="100",
            min_score="10",
            estimated_time="2 weeks"
        )

