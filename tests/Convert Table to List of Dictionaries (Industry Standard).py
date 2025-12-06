from utils.base import Base
from selenium.webdriver.common.by import By

class TestConvertTableToDict(Base):

    def test_convert_table_to_dict(self):
        # Step 1: Setup
        self.setup()
        driver = self.driver

        driver.get("https://omayo.blogspot.com")

        # Step 2: Locate table
        table = driver.find_element(By.ID, "table1")
        rows = table.find_elements(By.TAG_NAME, "tr")

        # Extract headers
        headers = [h.text for h in rows[0].find_elements(By.TAG_NAME, "th")]

        data_list = []

        # Step 3: Convert each row to dictionary
        for row in rows[1:]:
            cols = row.find_elements(By.TAG_NAME, "td")
            row_dict = {headers[i]: cols[i].text for i in range(len(cols))}
            data_list.append(row_dict)

        print("\nConverted Table Dictionary List:\n", data_list)

        # Step 4: Validation
        assert data_list[0]["Name"] == "Kishore", "First row Name mismatch"
        assert data_list[1]["Age"] == "25", "Second row Age mismatch"

        # Step 5: Screenshot
        self.screenshot("table_to_dict")

        # Step 6: Teardown
        self.teardown()
