import pytest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestUi():
    def setup_method(self):
        service=ChromeService(ChromeDriverManager().install())
        self.driver=webdriver.Chrome()
        #self.driver=webdriver.Edge()

        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def test_home_button_color(self):
        element=self.driver.find_element(By.LINK_TEXT,"Home")
        color = self.driver.execute_script("return window.getComputedStyle(arguments[0]).color;", element)
        #print("Color:", color)
        assert color == "rgb(255, 165, 0)"

    def test_font_family(self):
        element=self.driver.find_element(By.CSS_SELECTOR,".left-sidebar > h2")
        font_family = self.driver.execute_script("return window.getComputedStyle(arguments[0]).fontFamily;", element)
        assert font_family == "Roboto, sans-serif", f"Expected font family 'Arial, sans-serif', but got {font_family}"

    def test_font_size(self):
            element=self.driver.find_element(By.CSS_SELECTOR,".panel:nth-child(1) > .panel-heading a")
            font_size = self.driver.execute_script("return window.getComputedStyle(arguments[0]).fontSize;", element)
            assert font_size == "14px", f"Expected font size '24px', but got {font_size}"

    def test_spelling(self):
         element=self.driver.find_element(By.CSS_SELECTOR,".features_items > .title")
         assert element.text=="FEATURED ITEMS"

    def test_hover_button_color_change(self):
        self.driver.find_element(By.LINK_TEXT, " Products").click()
        time.sleep(1)
        button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#submit_search")))
        initial_color = self.driver.execute_script("return window.getComputedStyle(arguments[0]).backgroundColor;", button)

        actions = ActionChains(self.driver)
        actions.move_to_element(button).perform()

        time.sleep(1)

        hovered_color = self.driver.execute_script("return window.getComputedStyle(arguments[0]).backgroundColor;", button)

        print("Initial color:", initial_color)
        print("Hovered color:", hovered_color)

        assert initial_color != hovered_color, f"Expected the color to change, but it stayed the same! Initial: {initial_color}, Hovered: {hovered_color}"
