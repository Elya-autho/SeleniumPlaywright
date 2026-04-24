from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_name_field(browser):



    driver.get('https://lms.threadqa.ru/xpath-practice-hub/basics')
    time.sleep (3)

    #ищем элемент по data-testing="username-field"
    name_field = driver.find_element(By.CSS_SELECTOR, "[data-testid='username-field']")
    assert name_field.is_displayed()

    placeholder = name_field.get_attribute("placeholder")

    assert placeholder == "Введите ваше имя"

    name_field.clear()
    time.sleep(2)

    name_field.send_keys("Филиппова Эльвина")
    time.sleep(2)

    name_field.clear()
    time.sleep(2)

    name_field.send_keys("Смирнов тест")
    time.sleep(2)

    assert name_field.get_attribute("value") == "Смирнов тест"
    time.sleep(2)


