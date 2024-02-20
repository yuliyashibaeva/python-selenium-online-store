from .product_page import ProductPage
from .locators import ProductEditPageLocators


class ProductEditPage(ProductPage):
    def click_update_cart_button(self):
        self.browser.find_element(*ProductEditPageLocators.UPDATE_CART_BUTTON).click()
