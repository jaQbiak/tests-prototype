import pytest

from tests.login.login_page import LoginPage


@pytest.mark.login
class TestLogin:
    @staticmethod
    def test_title(browser):
        page = LoginPage(browser)
        expected_title = "Google"
        actual_title = page.get_title_of_page()
        assert actual_title == expected_title, f"Title should be {expected_title}, but it's {actual_title}"
