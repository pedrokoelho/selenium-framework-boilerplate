"""
LOGIN INVALID TESTS

Test case 002: Negative username test
Test case 003: Negative password test
"""

import pytest
from pages.login_page import LoginPage

class TestLoginInvalid:

    @pytest.mark.login
    @pytest.mark.invalid
    def test_002_login_invalid_username(self, driver):

        # instantiating the class pages
        login_page = LoginPage(driver)

        # 1. Open page
        login_page.open()
        # 2. Type username incorrectUser into Username field
        # 3. Type password Password123 into Password field
        # 4. Push Submit button
        login_page.execute_login('incorrectUser', 'Password123')
        # 5. Verify error message is displayed
        assert login_page.is_red_banner_displayed(), 'Error msg was not displayed!'
        # 6. Verify error message text is Your username is invalid!
        assert login_page.get_error_msg_text() == 'Your username is invalid!', 'Captured error msg text does not match expected text!'

    @pytest.mark.login
    @pytest.mark.invalid
    def test_003_login_invalid_password(self, driver):

        # instantiating the class pages
        login_page = LoginPage(driver)

        # 1. Open page
        login_page.open()
        # 2. Type username student into Username field
        # 3. Type password incorrectPassword into Password field
        # 4. Push Submit button
        login_page.execute_login('student', 'incorrectPassword')
        # 5. Verify error message is displayed
        assert login_page.is_red_banner_displayed(), 'Error msg was not displayed!'
        # 6. Verify error message text is Your password is invalid!
        assert login_page.get_error_msg_text() == 'Your password is invalid!', 'Captured error msg text does not match expected text!'
