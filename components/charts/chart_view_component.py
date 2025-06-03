from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.identifier = identifier
        self.chart_type = chart_type
        self.view = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible_view(self):
        expect(self.view).to_be_visible()


