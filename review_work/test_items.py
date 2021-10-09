from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    button_basket = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert button_basket, 'Button "Add to basket" not found soryan!'
    time.sleep(15)
