from playwright.sync_api import Page

from pages.base_page import BasePage
from components.navigation.navbar_component import NavbarComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar_component = NavbarComponent(page)
        self.create_course_form_component = CreateCourseFormComponent(page)
        self.create_course_toolbar_view_component = CreateCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar_view_component = CreateCourseExercisesToolbarViewComponent(page)
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.image_upload_widget_component = ImageUploadWidgetComponent(page,'create-course-preview' )
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.preview_image_upload_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-upload-button'
        )
        self.preview_image_remove_button = page.get_by_test_id(
            'create-course-preview-image-upload-widget-remove-button'
        )
        self.preview_image_upload_input = page.get_by_test_id('create-course-preview-image-upload-widget-input')

    def check_visible_create_course_title(self):
        self.create_course_toolbar_view_component.check_visible_title()

    def check_disabled_create_course_button(self, is_create_course_disabled: bool = True):
        self.create_course_toolbar_view_component.check_visible_button(is_create_course_disabled)

    def click_create_course_button(self):
        self.create_course_toolbar_view_component.click_button()

    def fill_create_course_form(
            self,
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
    ):
        self.create_course_form_component.fill(title,estimated_time,description,max_score,min_score)

    def check_visible_create_course_form(
            self,
            title="",
            estimated_time="",
            description="",
            max_score="0",
            min_score="0"
    ):
        self.create_course_form_component.check_visible(title,estimated_time,description,max_score,min_score)

    def check_visible_exercises_title(self):
        self.create_course_exercises_toolbar_view_component.check_visible_title()

    def check_visible_create_exercise_button(self):
        self.create_course_exercises_toolbar_view_component.check_visible_button()

    def click_create_exercise_button(self):
        self.create_course_exercises_toolbar_view_component.click()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )