from .base_page import BasePage
from .locators import ProductListPageLocators


class ProductListPage(BasePage):
    def click_add_to_cart_button(self):
        self.browser.find_element(*ProductListPageLocators.ADD_TO_CART_BUTTON).click()

    def choose_color(self, color: str):
        self.browser.find_element(*self.__get_product_color_locator(color)).click()

    def choose_size(self, size: str):
        self.browser.find_element(*self.__get_product_size_locator(size)).click()

    @staticmethod
    def __get_product_size_locator(size: str) -> tuple:
        if size == "XS":
            return ProductListPageLocators.XS_SIZE
        elif size == "S":
            return ProductListPageLocators.S_SIZE
        elif size == "M":
            return ProductListPageLocators.M_SIZE
        elif size == "L":
            return ProductListPageLocators.L_SIZE
        elif size == "XL":
            return ProductListPageLocators.XL_SIZE
        else:
            return None

    @staticmethod
    def __get_product_color_locator(color: str) -> tuple:
        if color == "Blue":
            return ProductListPageLocators.BLUE_COLOR
        elif color == "Green":
            return ProductListPageLocators.GREEN_COLOR
        elif color == "Purple":
            return ProductListPageLocators.PURPLE_COLOR
        else:
            return None
