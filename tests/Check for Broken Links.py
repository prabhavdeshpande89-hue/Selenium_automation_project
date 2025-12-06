from utils.base import Base
from selenium.webdriver.common.by import By

class TestGetAllLinks(Base):

    def test_get_all_links(self):
        # Step 1: Setup browser
        self.setup()
        driver = self.driver

        driver.get("https://omayo.blogspot.com")

        # Step 2: Get all <a> tags
        links = driver.find_elements(By.TAG_NAME, "a")

        print("\n===== FOUND LINKS =====")
        valid_links = []

        for link in links:
            text = link.text.strip()
            href = link.get_attribute("href")

            print(f"{text}  -->  {href}")

            if href and href.startswith("http"):
                valid_links.append(href)

        print("\nTotal <a> tags found:", len(links))
        print("Valid Links:", len(valid_links))

        # Step 3: Assertions
        assert len(links) > 0, "No <a> elements found on page!"
        assert len(valid_links) > 0, "No valid clickable links found!"

        # Step 4: Screenshot
        self.screenshot("get_all_links")

        # Step 5: Close browser
        self.teardown()
