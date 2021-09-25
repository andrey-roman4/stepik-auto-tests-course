from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
    # Переходим на страницу поисковика Гугл
    url = 'https://www.google.ru/'
    browser = webdriver.Chrome()
    browser.get(url)
    #button = browser.find_element_by_xpath('//div[contains(text(), "I agree")]')
    #button.click()
    # В поисковую строку вводим поисковый запрос
    search_area = browser.find_element_by_tag_name('input[title="Search"]')
    search_area.send_keys('четыре лапы')
    search_area.send_keys(Keys.RETURN)
    # В списке результатов поиска находим интересующий нас магазин и переходим в него
    link_4lapy = browser.find_element_by_partial_link_text('Интернет-зоомагазин Четыре Лапы')
    link_4lapy.click()
    # Переход в раздел "Собаки" и выбор категории "Сухой корм"
    browser.find_element_by_css_selector('.b-menu__link[href="/catalog/sobaki/"]')
    dog_food_select = browser.find_element_by_tag_name('a[title="Корм для собак"]')
    dog_food_select.click()
    dry_food = browser.find_element_by_tag_name('a[title="Сухой корм"]')
    dry_food.click()
    # Выбор производителя и переход в выбранный товар
    filter_by_manufacturer = browser.find_element_by_tag_name('label[title="Happy Dog"]')
    filter_by_manufacturer.click()
    first_products = browser.find_element_by_xpath('//span[contains(text(), "Fit&Vital Maxi Adult")]')
    first_products.click()
    # Добавления товара в корзину
    add_basket = browser.find_element_by_class_name('b-counter-basket__basket-link')
    add_basket.click()





finally:
    time.sleep(30)
    browser.close()
    browser.quit()