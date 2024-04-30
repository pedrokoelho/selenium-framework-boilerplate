"""
Test case 1: Positive LogIn test

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

class TestLoginValid:

    @pytest.mark.login
    @pytest.mark.valid
    def test_login_valid(self, driver):

        # instantiating the class page
        login_page = LoginPage(driver)

        # 1. Open page
        login_page.open()
        # 2. Type username student into Username field
        # 3. Type password Password123 into Password field
        # 4. Push Submit button
        login_page.execute_login('student', 'Password123')
        # 5. Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        # 6. Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        # 7. Verify button Log out is displayed on the new page