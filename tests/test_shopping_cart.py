from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from test_data.links import PRODUCT_LIST_PAGE_LINK, NADIA_ELEMENTS_SHELL_PRODUCT_PAGE_LINK, CART_PAGE_LINK
import pytest


class TestProductAddToShoppingCart:
    @pytest.mark.smoke
    def test_product_should_be_added_to_cart_from_product_list_page(self, browser):
        product_list_page = ProductListPage(browser)
        product_list_page.open(PRODUCT_LIST_PAGE_LINK)
        product_list_page.choose_size("M")
        product_list_page.choose_color("Purple")
        product_list_page.click_add_to_cart_button()
        product_list_page.product_should_be_in_cart()

    def test_product_should_be_added_to_cart_from_product_page(self, browser):
        product_page = ProductPage(browser)
        product_page.open(NADIA_ELEMENTS_SHELL_PRODUCT_PAGE_LINK)
        product_page.choose_size("S")
        product_page.choose_color("Black")
        product_page.click_add_to_cart_button()
        product_page.product_should_be_in_cart()

    def test_product_data_in_cart_should_be_consistent(self, browser):
        size = "S"
        color = "Green"

        product_list_page = ProductListPage(browser)
        product_list_page.open(PRODUCT_LIST_PAGE_LINK)
        product_list_page.choose_size(size)
        product_list_page.choose_color(color)
        product_list_page.click_add_to_cart_button()
        product_list_page.wait_until_product_in_cart()
        cart_page = CartPage(browser)
        cart_page.open(CART_PAGE_LINK)
        cart_page.product_data_in_cart_should_be_consistent(size, color)
