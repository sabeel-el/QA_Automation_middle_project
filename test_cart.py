import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import re
import time

class TestCart():
    def setup_method(self):
        service=ChromeService(ChromeDriverManager().install())
        self.driver=webdriver.Chrome()
        #driver=webdriver.Edge()

        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def test_add_cart(self):
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(1)
        first_product = self.driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(4)')
        actions = ActionChains(self.driver)
        actions.move_to_element(first_product).perform()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(4) .product-overlay .btn").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()
        element = self.driver.find_element(By.ID, "cart_info")
        assert element.is_displayed()

    def test_delete_item(self):
        self.driver.execute_script("window.scrollTo(0,300)")
        time.sleep(1)
        first_product = self.driver.find_element(By.CSS_SELECTOR, '.col-sm-4:nth-child(4)')
        actions = ActionChains(self.driver)
        actions.move_to_element(first_product).perform()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(4) .product-overlay .btn").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        element = self.driver.find_element(By.ID, "cart_info")
        self.driver.find_element(By.CSS_SELECTOR, ".cart_quantity_delete").click()
        time.sleep(5)
        assert not element.is_displayed()

    def test_items_quantity(self):
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").clear()
        self.driver.find_element(By.ID, "quantity").send_keys("4")
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".disabled").text == "4"

    def test_subscription_section_visible(self):
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        self.driver.execute_script("window.scrollTo(0,200)")
        assert self.driver.find_element(By.CSS_SELECTOR, ".single-widget > h2").is_displayed()

    def test_total_price(self):
        self.driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(5) .choose a").click()
        self.driver.find_element(By.ID, "quantity").click()
        self.driver.find_element(By.ID, "quantity").clear()
        self.driver.find_element(By.ID, "quantity").send_keys("3")
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()
        single_price=self.driver.find_element(By.CSS_SELECTOR, ".cart_price > p").text
        single_price = int(re.search(r'\d+', single_price).group())
        count=self.driver.find_element(By.CSS_SELECTOR, ".disabled").text
        count = int(re.search(r'\d+', count).group())
        total=self.driver.find_element(By.CSS_SELECTOR, ".cart_total_price").text
        total = int(re.search(r'\d+', total).group())
        assert count*single_price==total 

    

    

    
  