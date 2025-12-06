import logging
from utils.base import Base
from selenium.webdriver.common.by import By

class TestLinkText(Base):

    def test_link_text(self):
        logging.info("=== Test: LINK TEXT selector ===")

        # STEP 1: initialize driver
        self.setup()
        driver = self.driver

        driver.get("https://omayo.blogspot.com")

        # STEP 2: click link
        driver.find_element(By.LINK_TEXT, "Selenium143").click()

        # STEP 3: assert navigation
        assert "selenium143" in driver.current_url.lower()

        logging.info("Link clicked")
