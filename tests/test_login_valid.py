"""
LOGIN VALID TEST

Test case 001: Positive LogIn test

1. Open page
2. Type username student into Username field
3. Type password Password123 into Password field
4. Push Submit button
5. Verify new page URL contains practicetestautomation.com/logged-in-successfully/
6. Verify new page contains expected text ('Congratulations' or 'successfully logged in')
7. Verify button Log out is displayed on the new page
"""
import pytest
from pages.login_page import LoginPage
from pages.logged_in_page import LoggedInPage

class TestLoginValid:

    @pytest.mark.login
    @pytest.mark.valid
    def test_001_login_valid(self, driver):

        # instantiating the class pages
        login_page = LoginPage(driver)
        logged_in_page = LoggedInPage(driver)

        # 1. Open page
        login_page.open()
        # 2. Type username student into Username field
        # 3. Type password Password123 into Password field
        # 4. Push Submit button
        login_page.execute_login('student', 'Password123')
        # 5. Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert logged_in_page.expected_url == logged_in_page.current_url, 'Captured URL does not match Expected URL'
        # 6. Verify new page contains expected text ('Logged In Successfully')
        assert logged_in_page.header == 'Logged In Successfully', 'Captured text does not match expected text'
        # 7. Verify button Log out is displayed on the new page
        assert logged_in_page.is_loggout_btn_displayed(), 'Log Out button was not displayed'