from selenium.webdriver.common.by import By


class ProductPageLocators:
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    NAME_PRODUCT = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    BUTTON_ADD_REVIEW = (By.CSS_SELECTOR, "a[id='write_review']")
    TITLE_REVIEW = (By.CSS_SELECTOR, "fieldset legend")
    NAME_PRODUCT_BASKET = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    ALERT_TEXT = (By.CSS_SELECTOR, "div[class='alertinner ']")
    WISH_LIST = (By.XPATH, "//button[contains(@class, 'wishlist')]")
    VIEW_BASKET = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    TITLE_BASKET = (By.XPATH, "//div[@class='page-header action']/h1")
    BUTTON_CHECKOUT = (By.XPATH, "//a[contains(@class, 'btn-block')]")
    TITLE_CHECKOUT = (By.XPATH, "//div[@class='sub-header']/h1")
