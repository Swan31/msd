*** Settings ***
Library           SeleniumLibrary
Resource          ../resources/eshop.resource


*** Test Cases ***
Add two most expensive items to cart
    [Documentation]  Add two most expensive items to cart from ereaders category.
    [Tags]  desc
    open browser to eshop
    eshop_sharedComponents.click ebook category button
    order ereaders by price and verify items order  price:desc
    add first two items to shopping cart
    verify items in shopping cart
    [Teardown]  close browser

Add two cheapest items to cart
    [Documentation]  Add two most cheapest items to cart from ereaders category.
    [Tags]  asc
    open browser to eshop
    eshop_sharedComponents.click ebook category button
    order ereaders by price and verify items order  price:asc
    add first two items to shopping cart
    verify items in shopping cart
    [Teardown]  close browser