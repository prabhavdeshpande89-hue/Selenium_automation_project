import logging
from utils.base import Base
from selenium.webdriver.common.by import By

class TestNameSelector(Base):

    def test_searchbox_by_name(self):
        self.setup()
        driver = self.driver
        driver.get("https://omayo.blogspot.com")

        element = driver.find_element(By.NAME, "q")
        element.send_keys("Using NAME selector")

        assert element.get_attribute("value") != ""
        logging.info("NAME selector validated")
        self.teardown()
