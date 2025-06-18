from playwright.sync_api import Page, expect
import allure
from components.base_component import BaseComponent
from elements.text import Text

class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_title = Text(page,'dashboard-toolbar-title-text', 'dashboard_title')


    @allure.step("Check visible Dashboard title")
    def check_visible(self):
        self.dashboard_title.check_visible()
        self.dashboard_title.check_have_text('Dashboard')