import pytest
from selenium import webdriver

@pytest.fixture
def browser():

    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture
def base_url():
    return 'https://lms.threadqa.ru/xpath-practice-hub/basics'


@pytest.fixture
def user_names():
    return {
        "first_name": "Филиппова Эльвина",
        "second_name": "Смирнов Иван",
        "placeholder": "Введите ваше имя"
    }