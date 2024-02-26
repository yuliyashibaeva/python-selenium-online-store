from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.product_edit_page import ProductEditPage
from test_data.links import PRODUCT_LIST_PAGE_LINK, NADIA_ELEMENTS_SHELL_PRODUCT_PAGE_LINK, CART_PAGE_LINK
import pytest


@pytest.mark.add
class TestProductAddToShoppingCart:
    @pytest.mark.smoke
    def test_product_should_be_added_to_cart_from_product_list_page(self, browser):
        product_list_page = ProductListPage(browser)
        product_list_page.open(PRODUCT_LIST_PAGE_LINK)
        product_list_page.select_size("M")
        product_list_page.select_colour("Purple")
        product_list_page.click_add_to_cart_button()
        product_list_page.success_message_should_be_present()
        product_list_page.products_quantity_should_be_equal_to()

    def test_product_should_be_added_to_cart_from_product_page(self, browser):
        product_page = ProductPage(browser)
        product_page.open(NADIA_ELEMENTS_SHELL_PRODUCT_PAGE_LINK)
        product_page.select_size("S")
        product_page.select_colour("Black")
        product_page.click_add_to_cart_button()
        product_page.success_message_should_be_present()
        product_page.products_quantity_should_be_equal_to()

    def test_product_data_in_cart_should_be_consistent(self, browser):
        size = "S"
        color = "Green"

        product_list_page = ProductListPage(browser)
        product_list_page.open(PRODUCT_LIST_PAGE_LINK)
        product_list_page.select_size(size)
        product_list_page.select_colour(color)
        product_list_page.click_add_to_cart_button()
        product_list_page.wait_until_counter_number_is_not_empty()
        cart_page = CartPage(browser)
        cart_page.open(CART_PAGE_LINK)
        cart_page.product_data_in_cart_should_be_consistent(size, color)


@pytest.mark.update
class TestShoppingCartUpdating:
    def test_items_qty_should_be_updated(self, browser):
        product_list_page = ProductListPage(browser)
        product_list_page.open(PRODUCT_LIST_PAGE_LINK)
        product_list_page.select_size("XS")
        product_list_page.select_colour("Blue")
        product_list_page.click_add_to_cart_button()
        product_list_page.wait_until_counter_number_is_not_empty()

        cart_page = CartPage(browser)
        cart_page.open(CART_PAGE_LINK)
        items_qty_old = cart_page.get_items_qty_in_cart()
        items_qty_new = 2
        cart_page.update_items_qty(items_qty_new)
        cart_page.wait_until_counter_number_changes(items_qty_old)
        cart_page.products_quantity_should_be_equal_to(items_qty_new)

    def test_products_options_should_be_updated(self, browser):
        new_size = "L"
        new_color = "Yellow"

        product_page = ProductPage(browser)
        product_page.open(NADIA_ELEMENTS_SHELL_PRODUCT_PAGE_LINK)
        product_page.select_size("M")
        product_page.select_colour("Orange")
        product_page.click_add_to_cart_button()
        product_page.wait_until_counter_number_is_not_empty()

        cart_page = CartPage(browser)
        cart_page.open(CART_PAGE_LINK)
        cart_page.click_item_edit_button()

        product_edit_page = ProductEditPage(browser)
        product_edit_page.select_size(new_size)
        product_edit_page.select_colour(new_color)
        product_edit_page.click_update_cart_button()
        cart_page.success_message_should_be_present()
        cart_page.product_data_in_cart_should_be_consistent(new_size, new_color)


@pytest.mark.delete
class TestDeleteItemFromShoppingCart:
    def test_product_should_be_deleted_from_shopping_cart(self, browser):
        product_page = ProductPage(browser)
        product_page.open(NADIA_ELEMENTS_SHELL_PRODUCT_PAGE_LINK)
        product_page.select_size("L")
        product_page.select_colour("Yellow")
        product_page.click_add_to_cart_button()
        product_page.wait_until_counter_number_is_not_empty()
        cart_page = CartPage(browser)
        cart_page.open(CART_PAGE_LINK)
        cart_page.click_item_delete_button()
        cart_page.empty_cart_message_should_be_present()
        cart_page.cart_should_be_empty()
