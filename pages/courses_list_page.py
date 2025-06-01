from components.views.empty_view_component import EmptyViewComponent
from components.courses.courses_view_menu_component import CoursesViewMenuComponent
from components.courses.course_view_component import CourseViewComponent
from components.courses.courses_list_toolbar_view_component import CoursesListToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent

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

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

    def check_visible_empty_view(self):
        self.empty_view_component.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

