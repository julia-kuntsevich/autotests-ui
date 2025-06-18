import allure
from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text

class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page,f'{identifier}-empty-view-icon', 'Empty_view_icon')
        self.title = Text(page,f'{identifier}-empty-view-title-text', 'Empty_view_title')
        self.description = Text(page, f'{identifier}-empty-view-description-text', 'Empty_view_description')

    @allure.step('Check visible empty view "{title}"')
    def check_visible(self, title: str, description: str):
        self.icon.check_visible()
        self.title.check_visible()
        self.title.check_have_text(title)

        self.description.check_visible()
        self.description.check_have_text(description)