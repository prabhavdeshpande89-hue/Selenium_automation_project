from utils.base import Base
from selenium.webdriver.common.by import By

class TestGetAllLinks(Base):

    def test_get_all_links(self):
        # Step 1: Setup
        self.setup()
        driver = self.driver

        driver.get("https://omayo.blogspot.com")

        # Step 2: Find all <a> elements
        links = driver.find_elements(By.TAG_NAME, "a")

        print("\n===== Found Links =====")
        valid_links = 0

        for link in links:
            text = link.text.strip()
            href = link.get_attribute("href")

            print(f"{text} --> {href}")

            # Count only links with a valid URL
            if href and href.startswith("http"):
                valid_links += 1

        # Step 3: Assertions
        assert len(links) > 0, "No <a> tags found on the page"
        assert valid_links > 0, "No valid HTTP links found!"

        print(f"\nTotal <a> tags found: {len(links)}")
        print(f"Valid Links: {valid_links}")

        # Step 4: Screenshot
        self.screenshot("all_links")

        # Step 5: Teardown
        self.teardown()
