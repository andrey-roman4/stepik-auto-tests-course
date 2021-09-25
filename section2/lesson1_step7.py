from selenium import webdriver
import time
import math

url = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    img = browser.find_element_by_css_selector('img')
    x = img.get_attribute('valuex')
    y = calc(x)
    text_area = browser.find_element_by_css_selector('#answer')
    text_area.send_keys(y)
    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()
    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(15)
    browser.quit()
