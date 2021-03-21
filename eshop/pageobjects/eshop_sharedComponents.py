from PageObjectLibrary import PageObject
import time


class eshop_sharedComponents(PageObject):
    ebook_category = "st_advanced_ma_6"
    ebook_category_page_text = "//h1/span[contains(text(), 'Elektronické čtečky knih')]"
    shopping_cart_button = "id:blockcart_top_wrap"
    shopping_cart_item_count = "//a[@id='shopping_cart']/div//span[contains(@class, 'ajax_cart_quantity amount_circle')]"
    shopping_cart_item_check = "//a[@id='shopping_cart']/div//span[contains(text(), {item_count})]"

    def wait_for_eshop_homepage(self):
        """Wait until eshop homepage is loaded."""
        self.selib.wait_until_page_contains("Acomp", 10)

    def click_ebook_category_button(self):
        """Click ebook category button."""
        self.selib.click_element(self.ebook_category)
        self.selib.wait_until_page_contains_element(self.ebook_category_page_text, 10)

    def click_shopping_cart_button(self):
        """Click shopping cart button."""
        self.selib.click_element(self.shopping_cart_button)
        self.selib.wait_until_page_contains("Váš nákupní košík", 10)

    def get_shopping_cart_item_count(self):
        """Returns number of items in shopping cart."""
        return int(self.selib.get_text(self.shopping_cart_item_count))

    def verify_shopping_cart_item_count(self, item_count, timeout=5):
        """
        Verify that shopping cart item count is equal to given item count.
        :param item_count: expected number of items in shopping cart
        :param timeout: timeout in seconds
        :rtype boolean
        :returns true if expected number of items is in the shopping cart
        """
        i = 0
        verified = False
        while i <= timeout:
            shopping_cart_item_check_locator = self.shopping_cart_item_check.replace("{item_count}", str(item_count))
            verified = self.selib.get_element_count(shopping_cart_item_check_locator) > 0
            if verified:
                break
            else:
                time.sleep(1)
                i += 1
        if verified is False:
            print("Shopping cart item count was not verified!")
        return verified
