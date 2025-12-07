from utils.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestNewWindow(Base):

    def test_new_window_opens(self):
        # Step 1: Setup browser
        self.setup()
        driver = self.driver

        driver.get("https://omayo.blogspot.com")

        # Step 2: Click the link that opens a new window
        driver.find_element(By.LINK_TEXT, "SeleniumTutorial").click()

        # Step 3: Wait for new window to open
        self.wait.until(lambda d: len(d.window_handles) > 1)

        # Assertion: new window must exist
        assert len(driver.window_handles) > 1, "New window did NOT open!"

        # Step 4: Switch to new window
        driver.switch_to.window(driver.window_handles[1])

        # Step 5: Optional validation: check title or URL
        assert "selenium" in driver.current_url.lower(), "New window URL mismatch!"

        # Screenshot
        self.screenshot("new_window_opened")

        # Close test
        self.teardown()
