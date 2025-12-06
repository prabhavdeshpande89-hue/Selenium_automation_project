import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = driver.wait  # Using WebDriverWait from Base.py

    # -------------------------
    # Helper Method: Safe Click
    # -------------------------
    def safe_click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return True
        except Exception as e:
            logging.error(f"Click failed for {locator}: {e}")
            return False

    # -------------------------
    # Textarea
    # -------------------------
    def type_in_textarea(self, text):
        locator = (By.ID, "ta1")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # -------------------------
    # Search Box
    # -------------------------
    def type_in_searchbox(self, text):
        locator = (By.NAME, "q")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # -------------------------
    # Dropdown Button
    # -------------------------
    def click_dropdown_button(self):
        self.safe_click((By.CLASS_NAME, "dropbtn"))

    # -------------------------
    # Link Navigation
    # -------------------------
    def click_compendiumdev(self):
        self.safe_click((By.LINK_TEXT, "compendiumdev"))

    def click_testingblog(self):
        self.safe_click((By.PARTIAL_LINK_TEXT, "testingblog"))

    # -------------------------
    # Radio Buttons
    # -------------------------
    def select_radio_button1(self):
        self.safe_click((By.ID, "radio1"))

    def select_radio_button2(self):
        self.safe_click((By.ID, "radio2"))

    # -------------------------
    # Checkboxes
    # -------------------------
    def click_checkbox1(self):
        self.safe_click((By.ID, "checkbox1"))

    def click_checkbox2(self):
        self.safe_click((By.ID, "checkbox2"))

    # -------------------------
    # Single Select Dropdown
    # -------------------------
    def select_dropdown_by_visible_text(self, text):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, "drop1")))
        Select(element).select_by_visible_text(text)

    def select_dropdown_by_index(self, index):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, "drop1")))
        Select(element).select_by_index(index)

    def select_dropdown_by_value(self, value):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, "drop1")))
        Select(element).select_by_value(value)

    def get_selected_option(self):
        dropdown = Select(self.driver.find_element(By.ID, "drop1"))
        return dropdown.first_selected_option.text

    # -------------------------
    # Multi-select dropdown
    # -------------------------
    def select_multi_dropdown(self, values):
        element = self.wait.until(EC.visibility_of_element_located((By.ID, "multiselect1")))
        dropdown = Select(element)
        for val in values:
            dropdown.select_by_visible_text(val)

    def get_all_selected_options(self):
        dropdown = Select(self.driver.find_element(By.ID, "multiselect1"))
        return [opt.text for opt in dropdown.all_selected_options]

    def deselect_all_multiselect(self):
        dropdown = Select(self.driver.find_element(By.ID, "multiselect1"))
        dropdown.deselect_all()

    def is_multiselect(self):
        return Select(self.driver.find_element(By.ID, "multiselect1")).is_multiple

    # -------------------------
    # Iframe handling
    # -------------------------
    def enter_text_inside_iframe(self, text):
        try:
            self.wait.until(EC.frame_to_be_available_and_switch_to_it("iframe1"))
            inputs = self.driver.find_elements(By.TAG_NAME, "input")

            if inputs:
                inputs[0].send_keys(text)
            else:
                logging.warning("No input box found in iframe.")

        except Exception as e:
            logging.error(f"Iframe error: {e}")

        finally:
            self.driver.switch_to.default_content()

    # -------------------------
    # New Window Handling
    # -------------------------
    def open_new_window(self):
        self.safe_click((By.ID, "link1"))

    def switch_to_new_window(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    # -------------------------
    # Double Click
    # -------------------------
    def double_click_button(self):
        locator = (By.XPATH, "//button[text()='Double Click Me !!!']")
        button = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).double_click(button).perform()

    # -------------------------
    # Table Button
    # -------------------------
    def click_table_button(self):
        self.safe_click((By.XPATH, "//table//input[@value='submit']"))

    # -------------------------
    # Disabled Button Check
    # -------------------------
    def is_button_disabled(self):
        return not self.driver.find_element(By.ID, "but2").is_enabled()

    # -------------------------
    # Hidden Button (JS)
    # -------------------------
    def click_hidden_button(self):
        hidden = self.driver.find_element(By.ID, "hiddenbutton")
        self.driver.execute_script("arguments[0].click();", hidden)

    # -------------------------
    # Scrolling
    # -------------------------
    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    # -------------------------
    # Extract Table Text
    # -------------------------
    def get_table_text(self):
        table = self.wait.until(EC.visibility_of_element_located((By.ID, "table1")))
        return table.text
