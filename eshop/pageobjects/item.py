from eshop_sharedComponents import eshop_sharedComponents


class item(eshop_sharedComponents):
    item = "//ul[@class='product_list grid row']/li[{item_number}]"
    item_buy = "//ul[@class='product_list grid row']/li[{item_number}]//span[contains(text(), 'Koupit')]"
    item_code = "//ul[@class='product_list grid row']/li[{item_number}]//span[contains(text(), 'Kód:')]"
    items_price = "//div[@class='product-container']//span[@itemprop='price'][1]"

    def get_items_price(self):
        """Get price from all items on first page."""
        items = self.selib.get_webelements(self.items_price)
        prices = []
        for shopping_item in items:
            price = self.selib.get_text(shopping_item)
            price = price.replace(" ", "")
            price = price.replace("Kč", "")
            prices.append(int(price))
        return prices

    def add_item_to_cart(self, item_number):
        """Add item to cart."""
        item_locator = self.item.replace("{item_number}", str(item_number))
        item_buy_locator = self.item_buy.replace("{item_number}", str(item_number))
        item_code_locator = self.item_code.replace("{item_number}", str(item_number))
        code_text = self.selib.get_text(item_code_locator)
        code_split = code_text.split(": ")
        code = code_split[1]
        item_count = self.get_shopping_cart_item_count()
        self.selib.mouse_over(item_locator)
        self.selib.wait_until_element_is_visible(item_buy_locator, 5)
        self.selib.click_element(item_buy_locator)
        self.verify_shopping_cart_item_count(item_count+1)
        return code
