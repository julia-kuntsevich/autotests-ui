from config import settings
import platform
import sys
import os
from pathlib import Path


def create_allure_environment_file():
    # Получаем информацию об операционной системе
    os_info = f"{platform.system()}, {platform.release()}"

    # Получаем информацию о версии Python
    python_version = sys.version

    # Убедимся, что директория для отчета существует
    os.makedirs(settings.allure_results_dir, exist_ok=True)

    # Создаем содержимое файла environment.properties
    properties = [f"os_info={os_info}", f"python_version={python_version}"]

    # Добавляем настройки из конфига
    if hasattr(settings, 'model_dump'):
        properties.extend([f'{key}={value}' for key, value in settings.model_dump().items()])
    else:
        properties.extend([f'{key}={value}' for key, value in vars(settings).items()])

    # Собираем все элементы в единую строку с переносами
    properties_str = '\n'.join(properties)

    # Открываем файл ./allure-results/environment.properties на запись
    with open(Path(settings.allure_results_dir) / 'environment.properties', 'w') as file:
        file.write(properties_str)