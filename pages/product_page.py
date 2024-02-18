from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_cart_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def choose_color(self, color: str):
        self.browser.find_element(*self.__get_product_color_locator(color)).click()

    def choose_size(self, size: str):
        self.browser.find_element(*self.__get_product_size_locator(size)).click()

    @staticmethod
    def __get_product_size_locator(size: str) -> tuple:
        if size == "XS":
            return ProductPageLocators.XS_SIZE
        elif size == "S":
            return ProductPageLocators.S_SIZE
        elif size == "M":
            return ProductPageLocators.M_SIZE
        elif size == "L":
            return ProductPageLocators.L_SIZE
        elif size == "XL":
            return ProductPageLocators.XL_SIZE
        else:
            return None

    @staticmethod
    def __get_product_color_locator(color: str) -> tuple:
        if color == "Black":
            return ProductPageLocators.BLACK_COLOR
        elif color == "Orange":
            return ProductPageLocators.ORANGE_COLOR
        elif color == "Yellow":
            return ProductPageLocators.YELLOW_COLOR
        else:
            return None