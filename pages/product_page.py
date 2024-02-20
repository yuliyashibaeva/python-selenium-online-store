from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_cart_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def choose_color(self, color: str):
        self.browser.find_element(*BasePage.get_color_locator(ProductPageLocators, color)).click()

    def choose_size(self, size: str):
        self.browser.find_element(*BasePage.get_size_locator(ProductPageLocators, size)).click()
