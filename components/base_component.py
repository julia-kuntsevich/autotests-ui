from typing import Pattern


from playwright.sync_api import Page, expect
from tools.logger import get_logger  # Импортируем get_logger

logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: Pattern[str]):
        logger.info(f"Начинается проверка текущего URL на соответствие шаблону: {expected_url.pattern}")
        try:
            expect(self.page).to_have_url(expected_url)
            logger.info("Проверка текущего URL прошла успешно.")
        except AssertionError as e:
            logger.error(f"Проверка текущего URL не удалась: {e}")
            raise






        # expect(self.page).to_have_url(expected_url)