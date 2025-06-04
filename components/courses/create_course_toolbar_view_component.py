from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text','title')
        self.create_course_button = Button(page, 'create-course-toolbar-create-course-button','button')

    def check_visible_title(self):
        # Проверка видимости заголовка
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

    def check_visible_button(self, is_create_course_disabled: bool = True):
        self.create_course_button.check_visible()
        self.create_course_button.check_disabled()

        # Проверка состояния кнопки в зависимости от аргумента
        if is_create_course_disabled:
            self.create_course_button.check_disabled()
        else:
            self.create_course_button.check_enabled()

    def click_button(self):
        self.create_course_button.click()