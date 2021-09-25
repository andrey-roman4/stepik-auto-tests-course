from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

url = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    button = browser.find_element_by_css_selector('#book')
    button.click()

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    text_area = browser.find_element_by_css_selector('#answer')
    text_area.send_keys(y)
    button = browser.find_element_by_css_selector('#solve')
    button.click()
finally:
    time.sleep(15)
    browser.quit()