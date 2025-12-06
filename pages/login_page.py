import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = driver.wait  # WebDriverWait from Base

        # Locators
        self.username_locator = (By.XPATH, "//input[@name='userid']")
        self.password_locator = (By.XPATH, "//input[@name='pswrd']")
        self.login_btn_xpath = (By.XPATH, "//input[@value='Login']")
        self.login_btn_css = (By.CSS_SELECTOR, "input[value='Login']")

    # -------------------------
    # Helper: Safe Send Keys
    # -------------------------
    def safe_send_keys(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            logging.info(f"Entered text into field: {locator}")
            return True
        except Exception as e:
            logging.error(f"Failed to send keys to {locator}: {e}")
            return False

    # -------------------------
    # ENTER USERNAME
    # -------------------------
    def enter_username(self, username):
        return self.safe_send_keys(self.username_locator, username)

    # -------------------------
    # ENTER PASSWORD
    # -------------------------
    def enter_password(self, password):
        return self.safe_send_keys(self.password_locator, password)

    # -------------------------
    # CLICK LOGIN (XPATH)
    # -------------------------
    def click_login_xpath(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.login_btn_xpath))
            btn.click()
            logging.info("Clicked Login button (XPath)")
            return True
        except Exception as e:
            logging.error(f"Login button click failed (XPath): {e}")
            return False

    # -------------------------
    # CLICK LOGIN (CSS)
    # -------------------------
    def click_login_css(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.login_btn_css))
            btn.click()
            logging.info("Clicked Login button (CSS)")
            return True
        except Exception as e:
            logging.error(f"Login button click failed (CSS): {e}")
            return False

    # -------------------------
    # ALERT HANDLER
    # -------------------------
    def accept_alert_if_present(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            text = alert.text
            alert.accept()
            logging.info(f"Alert handled successfully: {text}")
            return text
        except Exception:
            logging.warning("No alert present")
            return None
