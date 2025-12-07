from utils.base import Base
from selenium.webdriver.common.by import By

class TestPartialLinkText(Base):

    def test_partial_link(self):
        self.setup()
        driver = self.driver
        driver.get("https://omayo.blogspot.com")

        driver.find_element(By.PARTIAL_LINK_TEXT, "testingblog").click()

        assert driver.current_url != ""
        self.teardown()
