from selenium import webdriver
import time
import os

url = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(url)
    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys('Ivan')
    surname = browser.find_element_by_css_selector('[name="lastname"]')
    surname.send_keys('Petrov')
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('ivan_petrov@example.com')
    upload_button = browser.find_element_by_css_selector('#file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    upload_button.send_keys(file_path)
    button = browser.find_element_by_css_selector('.btn')
    button.click()
finally:
    time.sleep(15)
    browser.quit()