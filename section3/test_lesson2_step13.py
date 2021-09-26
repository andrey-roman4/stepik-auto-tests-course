import unittest
from selenium import webdriver
import time

class TestRegist(unittest.TestCase):
    def test_reg1(self):
        try:
            url = 'http://suninjuly.github.io/registration1.html'
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

            self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'No welcome text')

        finally:
            time.sleep(10)
            browser.quit()


    def test_reg2(self):
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

            self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!', 'No welcome text')

        finally:
            time.sleep(10)
            browser.quit()

if __name__ == "__main__":
    unittest.main()
