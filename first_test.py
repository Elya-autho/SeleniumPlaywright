from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://lms.threadqa.ru/xpath-practice-hub')
time.sleep (3)
driver.quit()
