*** Settings ***
Documentation     Keywords for Acomp eshop
Library           SeleniumLibrary
Library           ../pageobjects/eshop_sharedComponents.py
Library           ../pageobjects/ereaders.py
Library           ../pageobjects/item.py
Library           ../pageobjects/shopping_cart.py
Library           Collections


*** Variables ***
${URL}      https://www.acomp.cz/
${BROWSER}        Chrome
${REMOTE_URL}      ${False}


*** Keywords ***
Open browser to eshop
    [Documentation]  Opens browser to eshop
    [Arguments]  ${url}=${URL}  ${browser}=${BROWSER}
    open browser    ${url}    ${browser}    remote_url=${REMOTE_URL}
    maximize browser window
    eshop_sharedComponents.wait for eshop homepage

Order ereaders by price and verify items order
    [Documentation]  Orders items in ereader category by price and verifies items order afterwards.
    [Arguments]  ${order_type}
    ${selected}  order items by   ${order_type}
    should be true  ${selected}  msg=Failed to select order items by price
    ${items_ordered}  verify items order by price   ${order_type}
    should be true  ${items_ordered}  msg=Failed to order by items by price

Add first two items to shopping cart
    [Documentation]  Adds first two items to shopping cart
    ${first_item_code}  ereaders.add item to cart  1
    ${second_item_code}  ereaders.add item to cart  2
    ${item_codes}  create list  ${first_item_code}  ${second_item_code}
    set test variable  ${item_codes}

Verify items in shopping cart
    [Documentation]  Verifies items were added to shopping cart
    eshop_sharedComponents.click shopping cart button
    ${shopping_cart_items}  create list
    FOR  ${item}  IN  @{item_codes}
        ${item_found}  verify shopping cart item by code  ${item}
        append to list  ${shopping_cart_items}  ${item_found}
    END
    should not contain  ${shopping_cart_items}  ${False}  msg=Item not found in shopping cart.