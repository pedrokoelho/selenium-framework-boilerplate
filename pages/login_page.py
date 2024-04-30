"""
Login Page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class LoginPage(BasePage):

    __url = 'https://practicetestautomation.com/practice-test-login/'

    # locators
    __txt_input_username = (By.NAME, 'username')
    __txt_input_password = (By.NAME, 'password')
    __btn_sumbit = (By.XPATH, '//button[@class="btn"]')
    __banner_error = (By.XPATH, '//div[@id="error"]')

    # contructor
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    # method to open the page
    def open(self):
        super()._open_url(self.__url)

    # method to execute login
    def execute_login(self, username: str, password: str):
        # 1. Type username into Username field
        super()._type(self.__txt_input_username, username)
        # 2. Type password into Password field
        super()._type(self.__txt_input_password, password)
        # 3. click button
        super()._click(self.__btn_sumbit)




    