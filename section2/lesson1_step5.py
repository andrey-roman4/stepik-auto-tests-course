from selenium import webdriver
import time
import math

url = 'http://suninjuly.github.io/math.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    text_area = browser.find_element_by_css_selector('#answer')
    text_area.send_keys(y)
    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton.click()
    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(15)
    browser.quit()