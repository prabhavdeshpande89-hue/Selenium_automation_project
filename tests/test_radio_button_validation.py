from utils.base import Base
from selenium.webdriver.common.by import By

class TestRadioButtons(Base):

    def test_radio_button1(self):
        self.setup()
        driver = self.driver
        driver.get("https://omayo.blogspot.com")

        radio1 = driver.find_element(By.ID, "radio1")
        radio1.click()

        assert radio1.is_selected()
        self.teardown()
