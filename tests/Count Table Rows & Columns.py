from utils.base import Base
from selenium.webdriver.common.by import By

class TestRowColumnCount(Base):

    def test_row_and_column_count(self):
        # Step 1: Start browser
        self.setup()
        driver = self.driver

        driver.get("https://omayo.blogspot.com/")

        # Step 2: Locate table
        table = driver.find_element(By.ID, "table1")

        # Step 3: Fetch rows
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Step 4: Fetch columns from first row
        header_cells = rows[0].find_elements(By.TAG_NAME, "th")

        # Step 5: Assertions
        assert len(rows) == 5, "Row count should be 5 (1 header + 4 rows)"
        assert len(header_cells) == 3, "Column count should be 3 (Name, Age, Place)"

        print(f"Total Rows Found: {len(rows)}")
        print(f"Total Columns Found: {len(header_cells)}")

        # Step 6: Screenshot
        self.screenshot("row_column_count")

        # Step 7: Teardown
        self.teardown()
