import pytest

@pytest.fixture
def clear_books_database() -> None:
    print("[FIXTURE] Удаляем данные из бд")

@pytest.fixture
def fill_books_database() -> None:
    print("[FIXTURES] Создаем новые данные в бд")

@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print("Reading all books")
