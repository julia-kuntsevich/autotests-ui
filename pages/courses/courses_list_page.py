from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_view_menu_component import CoursesViewMenuComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.courses.edit_course_form_component import EditCourseFormComponent

from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar_component = SidebarComponent(page)
        self.navbar_component = NavbarComponent(page)

        self.empty_view_component = EmptyViewComponent(page, 'courses-list')
        self.courses_view_menu_component = CoursesViewMenuComponent(page)
        self.course_view_component = CourseViewComponent(page)
        self.toolbar_view_component = CoursesListToolbarViewComponent(page)
        self.edit_course_form_component = EditCourseFormComponent(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible_empty_view(self):
        self.empty_view_component.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    def click_edit_course(self):
        self.courses_view_menu_component.click_edit()

    def edit_course_form(self):
        self.edit_course_form_component.fill(title,estimated_time,description,max_score,min_score)

    def check_visible_edited_form(self):
        self.edit_course_form_component.check_visible()



