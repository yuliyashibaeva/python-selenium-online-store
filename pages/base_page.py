from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def is_element_present(self, how, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_success_message_present(self) -> bool:
        return self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE)

    def open(self, link):
        self.browser.get(link)

    def product_should_be_in_cart(self):
        self.wait_until_product_in_cart()
        items_number = self.browser.find_element(*BasePageLocators.CART_PRODUCTS_NUMBER).text
        assert int(items_number) > 0 and self.is_success_message_present(), \
            "The product wasn't added to the cart."

    def wait_until_product_in_cart(self):
        WebDriverWait(self.browser, 5).until(
            lambda x: self.browser.find_element(*BasePageLocators.CART_COUNTER).get_attribute("class") == "counter qty"
        )
