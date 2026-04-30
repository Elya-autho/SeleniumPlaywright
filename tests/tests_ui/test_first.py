from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_name_field(browser, base_url, user_names):

    browser.get(base_url)

    #ищем элемент по data-testing="username-field"
    name_field = browser.find_element(By.CSS_SELECTOR, "[data-testid='username-field']")
    assert name_field.is_displayed()

    placeholder = name_field.get_attribute("placeholder")

    assert placeholder == user_names["placeholder"]

    name_field.clear()
    time.sleep(2)

    name_field.send_keys(user_names["first_name"])
    time.sleep(2)

    name_field.clear()
    time.sleep(2)

    name_field.send_keys(user_names["second_name"])
    time.sleep(2)

    assert name_field.get_attribute("value") == user_names["second_name"]
    time.sleep(2)


def test_registration(user_data):
    print((f""))


