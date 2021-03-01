*** Settings ***
Library           SeleniumLibrary
Resource          ../resources/eshop.resource


*** Test Cases ***
Add two most expensive items to cart
    [Documentation]  Add two most expensive items to cart from books category.
    open browser to eshop
    buy two most expensive ereaders
    [Teardown]  close browser