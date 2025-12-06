import logging
from utils.base import Base
from selenium.webdriver.common.by import By

class TestIDSelector(Base):

    def test_textarea_by_id(self):
        self.setup()
        driver = self.driver
        driver.get("https://omayo.blogspot.com")

        element = driver.find_element(By.ID, "ta1")
        element.send_keys("Testing ID selector")

        assert "Testing" in element.get_attribute("value")

        logging.info("ID selector working correctly")
        self.teardown()
