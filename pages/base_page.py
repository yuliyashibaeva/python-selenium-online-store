from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    # TODO: create cart base class and product base class

    def cart_should_be_empty(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_CART), "The cart isn't empty."

    @staticmethod
    def get_locator(locator_class_name, parameter: str) -> tuple:
        return getattr(locator_class_name, parameter.upper())

    @staticmethod
    def get_color_locator(locator_class_name, parameter: str) -> tuple:
        return BasePage.get_locator(locator_class_name, parameter + "_COLOR")

    @staticmethod
    def get_size_locator(locator_class_name, parameter: str) -> tuple:
        return BasePage.get_locator(locator_class_name, parameter + "_SIZE")

    def get_items_qty_in_cart(self) -> int:
        self.wait_until_counter_number_is_not_empty()
        items_qty = self.browser.find_element(*BasePageLocators.CART_PRODUCTS_NUMBER).text
        return int(items_qty)

    def products_quantity_should_be_equal_to(self, quantity: int = 1):
        items_qty = self.get_items_qty_in_cart()
        assert quantity == items_qty, \
            f"The number of products isn't correct.\nExpected: {quantity}, received: {items_qty}."

    def is_element_present(self, how, what: str) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def open(self, link):
        self.browser.get(link)

    def success_message_should_be_present(self):
        assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE), "There is no success message."

    def wait_until_counter_number_changes(self, initial_number: int):
        WebDriverWait(self.browser, 10).until(
            lambda x: self.get_items_qty_in_cart() != initial_number
        )

    def wait_until_counter_number_is_not_empty(self):
        WebDriverWait(self.browser, 10).until(
            lambda x: self.browser.find_element(*BasePageLocators.CART_PRODUCTS_NUMBER).text != ""
        )
