from selenium import webdriver
import time

try:
    url = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Chrome()
    browser.get(url)
    # Заполняем обязательные поля
    first_name = browser.find_element_by_css_selector('.first_class .first[required]')
    first_name.send_keys('First_Name')
    last_name = browser.find_element_by_css_selector('.second_class .second[required]')
    last_name.send_keys('Second_Name')
    email = browser.find_element_by_css_selector('.third_class .third[required]')
    email.send_keys('example@email.com')
    # Отправляем заполненную анкету
    submit_button = browser.find_element_by_css_selector('button.btn')
    submit_button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_css_selector('h1')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert welcome_text == 'Congratulations! You have successfully registered!'

finally:
    time.sleep(10)
    browser.quit()
