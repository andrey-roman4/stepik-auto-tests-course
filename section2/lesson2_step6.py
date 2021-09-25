from selenium import webdriver
import time
import math

url = 'http://suninjuly.github.io/execute_script.html'

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
    button = browser.find_element_by_css_selector('.btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]')
    radiobutton.click()
    button.click()

finally:
    time.sleep(15)
    browser.quit()
