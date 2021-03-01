from PageObjectLibrary import PageObject


class eshop(PageObject):
    ebook_category = "st_advanced_ma_6"
    ebook_category_page_text = "//h1/span[contains(text(), 'Elektronické čtečky knih')]"
    order_select = "selectProductSort"
    item = "//ul[@class='product_list grid row']/li[{item_number}]"
    item_buy = "//ul[@class='product_list grid row']/li[{item_number}]//span[contains(text(), 'Koupit')]"
    shopping_cart_item = "//a[@id='shopping_cart']/div//span[contains(text(), {item_number})]"
    loader = "//ul[@class='product_list grid row']/div[@id='layered_ajax_loader_inner']"

    def wait_for_eshop_homepage(self):
        """Wait until eshop homepage is loaded."""
        self.selib.wait_until_page_contains("Acomp", 10)

    def select_order_by_price_desc(self):
        """Select order items by price descending."""
        self.selib.select_from_list_by_value(self.order_select, "price:desc")
        selected_item = self.selib.get_selected_list_value(self.order_select)
        self.selib.wait_until_page_contains_element(self.loader, 10)
        self.selib.wait_until_page_does_not_contain_element(self.loader, 10)
        return selected_item == "price:desc"

    def click_ebook_category_button(self):
        """Click ebook category."""
        self.selib.click_element(self.ebook_category)
        self.selib.wait_until_page_contains_element(self.ebook_category_page_text, 10)

    def add_item_to_cart(self, item_number):
        """Add item to cart."""
        item_locator = self.item.replace("{item_number}", str(item_number))
        item_buy_locator = self.item_buy.replace("{item_number}", str(item_number))
        shopping_cart_item_locator = self.shopping_cart_item.replace("{item_number}", str(item_number))
        self.selib.mouse_over(item_locator)
        self.selib.wait_until_element_is_visible(item_buy_locator, 5)
        self.selib.click_element(item_buy_locator)
        self.selib.wait_until_page_contains_element(shopping_cart_item_locator, 10)
