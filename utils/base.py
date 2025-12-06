import os
import time
import logging
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base:
    """
    Professional Base class for Selenium Framework:
    - Browser setup
    - Logging
    - Explicit wait
    - Screenshot handling
    - Global slow-motion mode
    - Clean reusable find() helper
    """

    def setup(self):
        # -------------------------
        # LOGGING
        # -------------------------
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )
        logging.info("Initializing WebDriver...")

        # -------------------------
        # BROWSER OPTIONS
        # -------------------------
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-popup-blocking")

        # -------------------------
        # DRIVER INITIALIZATION
        # -------------------------
        self.driver = webdriver.Chrome(options=chrome_options)

        # -------------------------
        # GLOBAL WAITS
        # -------------------------
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 12)

        # -------------------------
        # SLOW MOTION MODE
        # -------------------------
        self.SLOW_MOTION = 0.6  # delay each action for visibility

        logging.info("WebDriver initialized successfully.")

    # -------------------------------------------
    # GLOBAL PAUSE (slows down execution)
    # -------------------------------------------
    def pause(self):
        time.sleep(self.SLOW_MOTION)

    # -------------------------------------------
    # UNIVERSAL FIND WITH EXPLICIT WAIT
    # -------------------------------------------
    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def teardown(self):
        logging.info("Closing browser...")
        try:
            time.sleep(1.2)
            self.driver.quit()
        except Exception as e:
            logging.error(f"Error during teardown: {e}")

    def screenshot(self, name):
        folder = r"C:\Users\prabh\PycharmProjects\Project\screenshots"

        if not os.path.exists(folder):
            os.makedirs(folder)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(folder, f"{name}_{timestamp}.png")

        self.driver.save_screenshot(file_path)
        logging.info(f"Screenshot saved: {file_path}")
