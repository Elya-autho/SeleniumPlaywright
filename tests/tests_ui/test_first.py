from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_name_field(self):

    driver = webdriver.Chrome()

    driver.get('https://lms.threadqa.ru/xpath-practice-hub')
    time.sleep (3)
    #ищем элемент по data-testing="username-field"
    driver.find_element((By.))
    driver.quit()
