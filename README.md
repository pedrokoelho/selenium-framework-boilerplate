# Framework Boilerplate with Selenium and Python


##### Created during the Udemy Course - [Selenium WebDriver: Selenium Automation Testing with Python](https://www.udemy.com/course/selenium-webdriver-python-course/)


#### Implementing the Design Pattern -> POM

***

#### Selenium

#### Pytest

###### tests folder with conftest file with driver fixture

    > tests
        > conftest.py

###### pages folder with a base page containing the basic methods common to all the pages

    > pages
        > base_page

###### basic page objects 

    > pages
        > login_page
        > logged_in_page

###### init file to tests folder and 3 basic login tests -> valid and invalid login

    > tests
        > __init__.py # creating this init file so we don't get an error executing the tests
        > test_login_valid 
        > test_login_invalid

###### pytest.ini to register the pytest markers

***

##### Executing the tests

`pytest -s -m valid` or `pytest -s -m login` # execute tests with markers

`pytest -s` # execute all tests


