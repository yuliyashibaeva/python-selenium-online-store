from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def click_item_delete_button(self):
        self.browser.find_element(*CartPageLocators.ITEM_DELETE_BUTTON).click()

    def click_item_edit_button(self):
        self.browser.find_element(*CartPageLocators.ITEM_EDIT_BUTTON).click()

    def empty_cart_message_should_be_present(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MSG), "There is no empty cart message."

    def __get_product_info(self) -> dict:
        product_info = {}
        item_options = self.browser.find_elements(*CartPageLocators.ITEM_OPTIONS)
        product_info["size"] = item_options[0].text
        product_info["color"] = item_options[1].text
        return product_info

    def product_data_in_cart_should_be_consistent(self, initial_size: str, initial_color: str):
        product_info = self.__get_product_info()
        assert product_info["size"] == initial_size and product_info["color"] == initial_color, \
            (f"The product data in the cart isn't consistent.\n"
             f"Received: size '{product_info['size']}', color 'product_info['color']'.\n"
             f"Expected: size '{initial_size}', color '{initial_color}'.'n")

    def update_items_qty(self, items_qty_new: int):
        self.browser.find_element(*CartPageLocators.QTY_INPUT).clear()
        self.browser.find_element(*CartPageLocators.QTY_INPUT).send_keys(items_qty_new)
        self.browser.find_element(*CartPageLocators.UPDATE_CART_BUTTON).click()
