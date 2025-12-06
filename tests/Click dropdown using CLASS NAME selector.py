from utils.base import Base
from selenium.webdriver.common.by import By

class TestClassSelector(Base):

    def test_dropdown_click(self):
        self.setup()
        driver = self.driver
        driver.get("https://omayo.blogspot.com")

        dropdown_btn = driver.find_element(By.CLASS_NAME, "dropbtn")
        dropdown_btn.click()

        assert dropdown_btn.is_displayed()
        self.teardown()
