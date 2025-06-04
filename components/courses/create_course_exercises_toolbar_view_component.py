from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button

class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_title = Text(page,'create-course-exercises-box-toolbar-title-text','exercises_title')
        self.create_exercise_button = Button(page,'create-course-exercises-box-toolbar-create-exercise-button','create_button')

    def check_visible_title(self):
        self.exercises_title.check_visible()
        self.exercises_title.check_have_text('Exercises')

    def check_visible_button(self):
        self.create_exercise_button.check_visible()

    def click(self):
        self.create_exercise_button.click()