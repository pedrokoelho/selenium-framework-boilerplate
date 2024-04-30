"""
Base Page
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class BasePage:

    # constructor
    def __init__(self, driver: WebDriver):
        self._driver = driver

    # Method to return the current url - it's public > we can access it from the tests
    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    # method to navigate to the url
    def _open_url(self, url: str):
        self._driver.get(url)

    # Method to find the element
    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    # Method to wait until the element is visible
    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    # Method to type text
    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    # Method to get the text
    def _get_text(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    # Method to click on the element
    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    # Method to verify if the element is displayed
    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

