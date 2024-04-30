"""
Login Page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class LoggedInPage(BasePage):

    __url = 'https://practicetestautomation.com/logged-in-successfully/'

    # locators
    __h1_title = (By.XPATH, '//h1[@class="post-title"]')
    __btn_log_out = (By.XPATH, '//a[contains(text(), "Log out")]')

    # contructor
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    # method to get the expected url
    @property
    def expected_url(self) -> str:
        return self.__url
    
    # method to get the h1 text
    @property
    def header(self) -> str:
        return super()._get_text(self.__h1_title)
    
    # method to verify if elemet is displayed
    def is_loggout_btn_displayed(self) -> bool:
        return super()._is_displayed(self.__btn_log_out)
