from .base_page import BasePage
from .locators import ProductListPageLocators


class ProductListPage(BasePage):
    def click_add_to_cart_button(self):
        self.browser.find_element(*ProductListPageLocators.ADD_TO_CART_BUTTON).click()

    def choose_color(self, color: str):
        self.browser.find_element(*BasePage.get_color_locator(ProductListPageLocators, color)).click()

    def choose_size(self, size: str):
        self.browser.find_element(*BasePage.get_size_locator(ProductListPageLocators, size)).click()
