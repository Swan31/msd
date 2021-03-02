# Coding assigment
> Write a program in any programming language that counts backwards from value provided by user to 1 and prints: “Agile” if the number is divisible by 5, “Software” if the
number is divisible by 3, “Testing” if the number is divisible by both,
or prints just the number if none of those cases are true.

## Solution
* Located in "countdown" directory, "countdown.py" file
* Written and tested in Python 3.9.2
* Run the python file and enter number when prompted
* There are input checks for natural number:
	* Negative numbers check, e.g. -5
	* Real numbers check, e.g. 5.5
	* Zero value check, e.g. 0
	* Non-number input check, e.g. xcg
    
# Test automation assigment
> Use your most preferred test automation framework to automate test without using automation recorders or code generators:
Go to your favorite e-shop, navigate to some category and add two
most expensive items to the shopping cart from this category.
Provide code from implementation.

## Solution
### Test case
* Go to eshop - https://www.acomp.cz/
* Go to e-readers category
* Add two most expensive e-readers to shopping cart

### Requirements
* Written in Python and Robot Framework
* Requirements with tested versions:
    * Python 3.9.2
    * robotframework 3.2.2
    * robotframework-seleniumlibrary 5.1.0
    * robotframework-pageobjectlibrary 1.0.2
    * selenium 3.141.0 or 4.0.0.b1
    * Chrome with matching release of chromedriver - 88.0.4324.190
### Structure
* Located in "eshop" directory
* pageobjectes - element locators with methods to interact with them
* resources - Robot Framework keywords
* testsuites - Robot Framework test
### Run test
* run test from "eshop.robot" file
* test can be run locally (default option) or remotely
* to run test remotely:
   * set robot variable "REMOTE" to "True"
   * set robot variable "REMOTE_URL" to your selenium, e.g. http://172.17.0.2:4444/wd/hub
### Run test with Docker
* get and run selenium standalone with chrome image from Docker hub - https://hub.docker.com/r/selenium/standalone-chrome
* build image from Dockerfile in project root
* run project container with remote option and remote url set to the selenium container
