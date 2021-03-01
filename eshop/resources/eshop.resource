*** Settings ***
Documentation     Keywords for Acomp eshop
Library           SeleniumLibrary
Library           ../pageobjects/eshop.py


*** Variables ***
${URL}      https://www.acomp.cz/
${BROWSER}        Chrome
${REMOTE_URL}      http://localhost:4444/wd/hub
${REMOTE}           False


*** Keywords ***
Open browser to eshop
    [Documentation]  Opens browser to eshop
    [Arguments]  ${url}=${URL}  ${browser}=${BROWSER}  ${remote}=${REMOTE}
    run keyword if  "${remote}"=="${True}"  open browser    ${url}    ${browser}    remote_url=${REMOTE_URL}
    ...  ELSE  open browser    ${url}    ${browser}
    maximize browser window
    wait for eshop homepage

Buy two most expensive ereaders
    [Documentation]  Go to e-readers category and add two most expensive e-readers to shopping cart
    click ebook category button
    ${selected}  select order by price desc
    should be true  ${selected}  msg=Failed to order by items by price
    add item to cart  1
    add item to cart  2