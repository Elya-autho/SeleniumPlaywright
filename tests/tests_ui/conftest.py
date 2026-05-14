import pytest
from selenium import webdriver
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

fake = Faker('ru')

@pytest.fixture
def browser(base_url):

    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver

    driver.quit()


@pytest.fixture
def base_url():
    return 'https://lms.threadqa.ru/xpath-practice-hub/basics'




@pytest.fixture
def wait(browser):
    return WebDriverWait(browser,  10)



@pytest.fixture
def user_names():
    first_name = fake.name()
    second_name = fake.name_female()
    return {
        "first_name": first_name,
        "second_name": second_name,
        "placeholder": "Введите ваше имя"
    }

@pytest.fixture(params=[
    {"country": "Россия", "xpath": "//*[contains(text(), 'Россия')]"},
    {"country": "США", "xpath": "//*[contains(text(), 'США')]"},
    {"country": "Германия", "xpath": "//*[contains(text(), 'Германия')]"},
    {"country": "Франция", "xpath": "//*[contains(text(), 'Франция')]"}
])
def country_data(request):
    return request.param


@pytest.fixture(params=[
    {"email":fake.email(), "username":fake.name_male(), "password":fake.password()},
    {"email":fake.email(), "username":fake.name_male(), "password":fake.password()},
    {"email":fake.email(), "username":fake.name_male(), "password":fake.password()}
])
def user_data(request):
    return request.param

