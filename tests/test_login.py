from pages.login_page import LoginPage

ZEN_URL = "https://www.zenclass.in/login"
VALID_USERNAME = "yashkamdar88@gmail.com"
VALID_PASSWORD = "Yashkamdar@9"
INVALID_PASSWORD = "WrongPassword123"


# a. Successful Login
def test_successful_login(page):
    login = LoginPage(page)
    login.load(ZEN_URL)
    login.login(VALID_USERNAME, VALID_PASSWORD)
    page.wait_for_timeout(5000)
    assert "dashboard" in page.url.lower()


# b. Unsuccessful Login
def test_unsuccessful_login(page):
    login = LoginPage(page)
    login.load(ZEN_URL)
    login.login(VALID_USERNAME, INVALID_PASSWORD)
    page.wait_for_timeout(3000)
    assert "login" in page.url.lower()


# c. Validate Username & Password Fields
def test_validate_input_fields(page):
    login = LoginPage(page)
    login.load(ZEN_URL)
    login.validate_input_fields()


# d. Validate Submit Button
def test_validate_submit_button(page):
    login = LoginPage(page)
    login.load(ZEN_URL)
    login.validate_submit_button()


# e. Validate Logout Functionality
def test_logout_functionality(page):
    login = LoginPage(page)
    login.load(ZEN_URL)
    login.login(VALID_USERNAME, VALID_PASSWORD)
    page.wait_for_timeout(5000)
    login.logout()
    page.wait_for_timeout(3000)
    assert "login" in page.url.lower()



