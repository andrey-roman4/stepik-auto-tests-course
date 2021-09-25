from selenium import webdriver
import time
import math

url = 'http://suninjuly.github.io/alert_accept.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    start_button = browser.find_element_by_css_selector('.btn')
    start_button.click()
    confirm_window = browser.switch_to.alert
    confirm_window.accept()
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    text_area = browser.find_element_by_css_selector('#answer')
    text_area.send_keys(y)
    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(15)
    browser.quit()