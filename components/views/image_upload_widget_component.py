from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.image import Image
from elements.icon import Icon
from elements.text import Text
from elements.button import Button
from elements.file_input import FileInput


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        # Используем компонент EmptyViewComponent
        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(page,f'{identifier}-image-upload-widget-preview-image','preview_image')
        self.image_upload_info_icon = Icon(page,f'{identifier}-image-upload-widget-info-icon','image_upload_icon')
        self.image_upload_info_title = Text(page,f'{identifier}-image-upload-widget-info-title-text','info_title')
        self.image_upload_info_description = Text(
            page, f'{identifier}-image-upload-widget-info-description-text', 'upload_info_description'
        )

        self.upload_button = Button(page,f'{identifier}-image-upload-widget-upload-button', 'upload_button')
        self.remove_button = Button(page,f'{identifier}-image-upload-widget-remove-button', 'remove_button')
        self.upload_input = FileInput(page,f'{identifier}-image-upload-widget-input', 'upload_input')

        # Проверяет отображение виджета в зависимости от наличия загруженного изображения
    def check_visible(self, is_image_uploaded: bool = False):
        self.image_upload_info_icon.check_visible()
        self.image_upload_info_title.check_visible()
        self.image_upload_info_title.check_have_text(
            'Tap on "Upload image" button to select file'
        )

        self.image_upload_info_description.check_visible()
        self.image_upload_info_description.check_have_text('Recommended file size 540X300')
        self.upload_button.check_visible()

        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            self.remove_button.check_visible()
            self.preview_image.check_visible()
        if not is_image_uploaded:
            # Если картинка yt загружена, проверяем наличие компонента EmptyViewComponent
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)