from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

url = 'http://suninjuly.github.io/selects1.html'

def sum(x,y):
    return str(int(x) + int(y))


try:
    browser = webdriver.Chrome()
    browser.get(url)
    first_el= browser.find_element_by_css_selector('#num1')
    first_num = first_el.text
    second_el= browser.find_element_by_css_selector('#num2')
    second_num = second_el.text
    result = sum(first_num, second_num)
    select = Select(browser.find_element_by_css_selector('select'))
    select.select_by_value(result)
    button = browser.find_element_by_css_selector('.btn').click()

finally:
    time.sleep(15)
    browser.quit()
