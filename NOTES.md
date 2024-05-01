## Create virtual environment
    
    `py -m venv `

## Activate the virtual env in bash

    `. venv/Scripts/activate`

## Initialize Git local repository

    `git init`

## Install Selenium

    `pip install -U selenium`

## Install Pytest

    `pip install pytest`


## Create tests folder and inside create conftest file with driver fixture

    > tests
        > conftest.py

## Create pages folder and create base page

    > pages
        > base_page

## Create the page objects 

    > pages
        > login_page
        > logged_in_page

## Create the tests

    > tests
        > __init__.py # create this init file so we don't get an error executing the tests
        > test_login_valid

## Create pytest.ini to register the pytest markers

## Execute the tests

`pytest -s -m valid` or `pytest -s -m login` # execute tests with markers

`pytest -s` # execute all tests
