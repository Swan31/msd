from eshop_sharedComponents import eshop_sharedComponents


class shopping_cart(eshop_sharedComponents):
    shopping_cart_item_code = "//td[@class='cart_description']//span[contains(text(), '{item_number}')]"

    def verify_shopping_cart_item_by_code(self, code):
        """Verify shopping cart item by given code."""
        shopping_cart_item_code_locator = self.shopping_cart_item_code.replace("{item_number}", code)
        return self.selib.get_element_count(shopping_cart_item_code_locator) > 0
