import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC

from tests.tests_ui.conftest import browser


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_name_field(browser, base_url, user_names,wait):

    browser.get(base_url)
    name_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='username-field']")))
    #ищем элемент по data-testing="username-field"

    # name_field = browser.find_element(By.CSS_SELECTOR, "[data-testid='username-field']")


    wait.until(EC.visibility_of(name_field))
    assert name_field.is_displayed()

    placeholder = name_field.get_attribute("placeholder")

    assert placeholder == user_names["placeholder"]

    name_field.clear()

    name_field.send_keys(user_names["first_name"])

    name_field.clear()


    name_field.send_keys(user_names["second_name"])
    wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,"[data-testid='username-field']"), user_names["second_name"]))


    assert name_field.get_attribute("value") == user_names["second_name"]


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_email_field_validation(browser, wait,base_url,browser_get):


    email_field = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"[data-testid='email-field']"))
    )
    valid_email = "user@example.com"
    email_field.send_keys(valid_email)

    assert email_field.get_attribute("value") == valid_email
    assert email_field.get_attribute("type") == "email"

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_password_field_masking(browser, wait, base_url, browser_get):


    password_field = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='password-field']"))
    )

    test_password = "SecurePass123"
    password_field.clear()
    password_field.send_keys(test_password)

    # тип поля password
    assert password_field.get_attribute("type") == "password"

    # значение сохранилось
    assert password_field.get_attribute("value") == test_password

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_area_multilaine_input(browser, wait, base_url, browser_get):
    textarea = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='comment-field']"))
    )
    multiline_text = "Введите ваш комментарий..\nВторая строка\nТретья строка"
    textarea.send_keys(multiline_text)

    assert  textarea.get_attribute("value") == multiline_text

@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_dropdown_selection(browser,wait, base_url, browser_get):
    dropdown_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='country-dropdown']"))
    )

    initial_text = dropdown_button.text
    #print(dropdown_button.text)
    assert initial_text == "Выберите страну"

    dropdown_button.click()

    usa_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'США')]"))
    )
    usa_option.click()

    assert "США" in dropdown_button.text

    dropdown_button.click()

    germany_option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Германия')]"))
    )
    germany_option.click()

    assert "Германия" in dropdown_button.text

def test_toggle_checkbox(browser, wait, base_url, browser_get):

    checkbox = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid=terms-agreement']"))
    )
    checkbox.click()

    assert checkbox.is_selected()
    









@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_registration(user_data):
    print(f"Email:{user_data['email']}")
    print(f"Username: {user_data['username']}")


