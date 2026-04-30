import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

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

@pytest.fixture(params=[
    {"email":"test1@mail.ru", "username":"user25", "password":"pass1",
     "email":"test2@mail.ru", "username":"user26", "password":"pass2",
    "email":"test3@mail.ru", "username":"user27", "password":"pass3"}
])
def user_data(request):
    return request.param

