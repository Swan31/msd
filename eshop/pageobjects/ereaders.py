from item import item


class ereaders(item):
    order_select = "selectProductSort"
    shopping_cart_item = "//a[@id='shopping_cart']/div//span[contains(text(), {item_number})]"
    loader = "//ul[@class='product_list grid row']/div[@id='layered_ajax_loader_inner']"

    def order_items_by(self, sort_order):
        """Select given sort order for items on the page"""
        self.selib.select_from_list_by_value(self.order_select, sort_order)
        selected_item = self.selib.get_selected_list_value(self.order_select)
        self.selib.wait_until_page_contains_element(self.loader, 10)
        self.selib.wait_until_page_does_not_contain_element(self.loader, 10)
        return selected_item == sort_order

    def verify_items_order_by_price(self, sort_order):
        """Verifies items order by price."""
        items_prices = item.get_items_price(self)
        if sort_order == "price:desc":
            return items_prices[1] >= items_prices[-1]
        elif sort_order == "price:asc":
            return items_prices[1] <= items_prices[-1]
