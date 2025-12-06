from utils.base import Base
from selenium.webdriver.common.by import By

class TestReadTable(Base):

    def test_read_full_table(self):
        self.setup()
        driver = self.driver

        driver.get("https://omayo.blogspot.com/")

        table = driver.find_element(By.ID, "table1")
        table_text = table.text

        print("\n===== FULL TABLE CONTENT =====")
        print(table_text)
        print("==============================\n")

        # Validate data that exists
        assert "Kishore" in table_text
        assert "Manish" in table_text
        assert "Delhi" in table_text
        assert "Pune" in table_text

        self.screenshot("table1_read")
        self.teardown()
