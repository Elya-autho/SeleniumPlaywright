from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC


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
    time.sleep(2)

    name_field.clear()
    time.sleep(2)

    name_field.send_keys(user_names["second_name"])
    wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR,"[data-testid='username-field']"), user_names["second_name"]))


    assert name_field.get_attribute("value") == user_names["second_name"]
    time.sleep(2)


def test_registration(user_data):
    print(f"Email:{user_data['email']}")
    print(f"Username: {user_data['username']}")


