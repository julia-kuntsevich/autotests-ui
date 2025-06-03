from playwright.sync_api import Page

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.charts.chart_view_component import ChartViewComponent
from components.charts.title_component import TitleComponent
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)


        self.sidebar_component = SidebarComponent(page)
        self.navbar_component = NavbarComponent(page)
        self.dashboard_toolbar_view_component = DashboardToolbarViewComponent(page)

        self.scores_title = TitleComponent(page, "scores")
        self.courses_title = TitleComponent(page, "courses")
        self.students_title = TitleComponent(page, "students")
        self.activities_title = TitleComponent(page, "activities")

        self.scores_chart_view = ChartViewComponent(page, "scores", "scatter")
        self.courses_chart_view = ChartViewComponent(page, "courses", "pie")
        self.students_chart_view = ChartViewComponent(page, "students", "bar")
        self.activities_chart_view = ChartViewComponent(page, "activities", "line")

    def check_dashboard_title(self):
        self.dashboard_toolbar_view_component.check_visible()

    def check_visible_scores_title(self):
        self.scores_title.check_visible_title("Scores")

    def check_visible_courses_title(self):
        self.scores_title.check_visible_title("Courses")

    def check_visible_students_title(self):
        self.scores_title.check_visible_title("Students")

    def check_visible_activities_title(self):
        self.scores_title.check_visible_title("Activities")

    def check_visible_scores_chart(self):
        self.scores_chart_view.check_visible_view()

    def check_visible_courses_chart(self):
        self.courses_chart_view.check_visible_view()

    def check_visible_students_chart(self):
        self.students_chart_view.check_visible_view()

    def check_visible_activities_chart(self):
        self.activities_chart_view.check_visible_view()