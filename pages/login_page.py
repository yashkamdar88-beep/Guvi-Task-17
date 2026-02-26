from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from pages.login_locators import LoginLocators


class LoginPage:

    def __init__(self, page):
        self.page = page
        self.locators = LoginLocators()

    def load(self, url):
        try:
            self.page.goto(url, timeout=60000)
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_selector(
                self.locators.USERNAME_INPUT,
                state="visible",
                timeout=20000
            )
        except PlaywrightTimeoutError:
            print("Page did not load properly")
            raise

    def login(self, username, password):
        self.page.fill(self.locators.USERNAME_INPUT, username)
        self.page.fill(self.locators.PASSWORD_INPUT, password)
        self.page.click(self.locators.LOGIN_BUTTON)

        # Wait for dashboard to load
        self.page.wait_for_load_state("networkidle")

        # Handle popup if present
        self.close_popup_if_present()

    def close_popup_if_present(self):
        try:
            if self.page.locator(self.locators.POPUP_CLOSE_BUTTON).is_visible(timeout=5000):
                self.page.click(self.locators.POPUP_CLOSE_BUTTON)
        except:
            # If popup not present, continue silently
            pass

    def validate_input_fields(self):
        try:
            self.page.wait_for_selector(self.locators.USERNAME_INPUT, timeout=10000)
            self.page.wait_for_selector(self.locators.PASSWORD_INPUT, timeout=10000)

            assert self.page.is_visible(self.locators.USERNAME_INPUT)
            assert self.page.is_visible(self.locators.PASSWORD_INPUT)

        except Exception as e:
            print("Input field validation failed:", e)
            raise

    def validate_submit_button(self):
        try:
            self.page.wait_for_selector(self.locators.LOGIN_BUTTON, timeout=10000)
            assert self.page.is_enabled(self.locators.LOGIN_BUTTON)

        except Exception as e:
            print("Submit button validation failed:", e)
            raise

    def logout(self):
        try:
            self.page.wait_for_load_state("networkidle")

            self.page.wait_for_selector(self.locators.POPUP_CLOSE_BUTTON, timeout=50000)
            self.page.click(self.locators.POPUP_CLOSE_BUTTON)
            # Click avatar/profile icon
            self.page.wait_for_selector(self.locators.PROFILE_ICON, timeout=15000)
            self.page.click(self.locators.PROFILE_ICON)

            # Now logout will become visible
            self.page.wait_for_selector(self.locators.LOGOUT_BUTTON, timeout=10000)
            self.page.click(self.locators.LOGOUT_BUTTON)

            # Confirm redirection to login page
            self.page.wait_for_url("**/login", timeout=15000)

        except Exception as e:
            print("Logout failed:", e)
            raise