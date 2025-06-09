from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea
from elements.button import Button


class EditCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.edit_course_title_input = Input(page,'create-course-form-title-input','title')
        self.edit_course_estimated_time_input = Input(
            page,'create-course-form-estimated-time-input','time'
        )
        self.edit_course_description_textarea = Textarea(
            page,'create-course-form-description-input','description'
        )
        self.edit_course_max_score_input = Input(page,'create-course-form-max-score-input','max_score')
        self.edit_course_min_score_input = Input(page,'create-course-form-min-score-input','min_score')
        self.update_course_button = Button(page, 'create-course-toolbar-create-course-button','button')

    def fill(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.edit_course_title_input.fill(title)
        self.edit_course_title_input.check_have_value(title)

        self.edit_course_estimated_time_input.fill(estimated_time)
        self.edit_course_estimated_time_input.check_have_value(estimated_time)

        self.edit_course_description_textarea.fill(description)
        self.edit_course_description_textarea.check_have_value(description)

        self.edit_course_max_score_input.fill(max_score)
        self.edit_course_max_score_input.check_have_value(max_score)

        self.edit_course_min_score_input.fill(min_score)
        self.edit_course_min_score_input.check_have_value(min_score)

    def check_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.edit_course_title_input.check_visible()
        self.edit_course_title_input.check_have_value(title)

        self.edit_course_estimated_time_input.check_visible()
        self.edit_course_estimated_time_input.check_have_value(estimated_time)

        self.edit_course_description_textarea.check_visible()
        self.edit_course_description_textarea.check_have_value(description)

        self.edit_course_max_score_input.check_visible()
        self.edit_course_max_score_input.check_have_value(max_score)

        self.edit_course_min_score_input.check_visible()
        self.edit_course_min_score_input.check_have_value(min_score)

    def click_button(self):
        self.update_course_button.click()


