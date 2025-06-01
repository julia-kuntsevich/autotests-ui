from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class TitleComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.identifier = identifier
        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')

    def check_visible_title(self, identifier):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(identifier)