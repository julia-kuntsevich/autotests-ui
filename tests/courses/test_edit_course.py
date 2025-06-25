import pytest
import allure
from tools.routes import AppRoute
from config import settings
from fixtures.pages import courses_list_page
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag

@pytest.mark.courses
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.COURSES)
@allure.sub_suite(AllureStory.COURSES)
class TestCourses:
    @allure.title("Edit course")
    def test_edit_course(
            self,
            create_course_page: CreateCoursePage,
            courses_list_page: CoursesListPage
    ):
        create_course_page.visit(AppRoute.COURSES_CREATE)
        create_course_page.create_course_form_component.fill(
            title="Playwright",
            estimated_time="2 weeks",
            description="Playwright",
            max_score="100",
            min_score="10"
        )
        create_course_page.image_upload_widget_component.upload_preview_image(settings.test_data.image_png_file)
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

