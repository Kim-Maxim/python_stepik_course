import pytest
import allure
import random

from selenium.webdriver.common.by import By

@allure.parent_suite("Интернет-магазин")
@allure.suite("Книги")
@allure.sub_suite("Страница продукта")
class TestProductPage:
    
    @allure.severity(allure.severity_level.MINOR)
    @allure.title("Проверка видимости кнопки 'Добавить в корзину'")
    @pytest.mark.smoke
    def test_button_add_to_basket_is_visible(self, browser):
        """ Тест проверяет наличие кнопки добавления в корзину """
        list = [
        "http://selenium1py.pythonanywhere.com/catalogue/studyguide-for-counter-hack-reloaded_205/",
        "http://selenium1py.pythonanywhere.com/catalogue/visual-guide-to-lock-picking_206/",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/",
        "http://selenium1py.pythonanywhere.com/catalogue/hacking-exposed-wireless_208/",
        "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        ]
        link = random.sample(list, k=1)
        browser.get(''.join(link))
        assert browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket"), "The button busket have been not found"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка наличия наименования товара на странице")
    @pytest.mark.smoke
    def test_check_name_product(self, browser):
        """ Тест проверяет наличие и наименование продукта на странице """   
        name_product = browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/h1").text
        assert len(name_product) > 0, "The page of product has been not loaded"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Проверка написания отзыва о товаре")
    @pytest.mark.smoke
    def test_write_review(self, browser):
        """ Тест проверяет возможность написания отзыва """
        button_review = browser.find_element(By.CSS_SELECTOR, "a[id='write_review']")
        button_review.click()
        title_review = browser.find_element(By.CSS_SELECTOR, "fieldset legend")
        assert title_review is not None, "The button of review is not clickable"

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Проверка добавление товара в корзину")
    @pytest.mark.smoke
    def test_add_product_in_basket(self, browser):
        """ Тест проверяет добавление товара в корзину """
        button_basket = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        button_basket.click()
        name_product = browser.find_element(By.XPATH, "//div[@class='col-sm-6 product_main']/h1").text
        alert_text = browser.find_element(By.CSS_SELECTOR, "div[class='alertinner ']").text
        assert name_product in alert_text, "The product has been not added"

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Проверка добавления товара в избранное")
    @pytest.mark.xfail(reason = 'Кнопка не кликабельна')
    def test_add_to_wish_list(self, browser):
        """ Тест проверяет добавление товара в избранное """
        wish_list = browser.find_element(By.XPATH, "//button[contains(@class, 'wishlist')]")
        wish_list.click()
        assert True, "The button of add to wish list is not clickable"

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Проверка перехода в корзину")
    @pytest.mark.smoke
    def test_open_backet(self, browser):
        """ Тест проверяет открытие корзины """
        view_basket = browser.find_element(By.CSS_SELECTOR, "a[class='btn btn-default']")
        view_basket.click()
        title_busket = browser.find_element(By.XPATH, "//div[@class='page-header action']/h1").text
        assert len(title_busket) > 0, "The page has been not loaded"
    
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Проверка перехода в оформление")
    @pytest.mark.smoke
    def test_proceed_to_checkout(self, browser):
        """ Тест проверяет переход к оформлению заказа """
        proceed_to_checkout = browser.find_element(By.XPATH, "//a[contains(@class, 'btn-block')]")
        proceed_to_checkout.click()
        title_checkout = browser.find_element(By.XPATH, "//div[@class='sub-header']/h1").text
        assert len(title_checkout) > 0, "The page has been not loaded"
