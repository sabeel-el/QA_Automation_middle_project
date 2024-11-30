import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestProducts():
    def setup_method(self, method):
        service=ChromeService(ChromeDriverManager().install())
        self.driver=webdriver.Chrome()
        #driver=webdriver.Edge()

        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
    
    def test_brand(self):
        self.driver.execute_script("window.scrollTo(0,300.79998779296875)")
        self.driver.find_element(By.CSS_SELECTOR, ".nav-stacked > li:nth-child(1) > a").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "BRAND - POLO PRODUCTS"

    def test_add_review(self):
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("sabeel")
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("sa@qa")
        self.driver.find_element(By.ID, "review").send_keys("great product")
        self.driver.find_element(By.ID, "button-review").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".alert-success > span").text == "Thank you for your review."

    def test_products_count(self):
        self.driver.execute_script("window.scrollTo(0,300.79998779296875)")
        self.driver.find_element(By.CSS_SELECTOR, ".nav-stacked > li:nth-child(1) > a").click()
        products = self.driver.find_elements(By.CLASS_NAME, 'single-products')
        visible_products = [p for p in products if p.is_displayed()]
        expected_product_count =6
        assert len(visible_products) == expected_product_count

    def test_search_saree(self):
        self.driver.find_element(By.CSS_SELECTOR, ".panel:nth-child(1) .fa").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".panel-body li:nth-child(3) > a").click()
        time.sleep(3)
        products = self.driver.find_elements(By.CSS_SELECTOR, '.productinfo.text-center p')
        for product in products:
            product_name = product.text.lower()  
            assert 'saree' in product_name, f"Product name '{product_name}' does not contain 'saree'."

        print(f"All {len(products)} products contain the word 'saree' in their name.")


    def test_search_dress(self):
        self.driver.find_element(By.LINK_TEXT, " Products").click()
        self.driver.find_element(By.ID, "search_product").click()
        self.driver.find_element(By.ID, "search_product").send_keys("dress")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-search").click()
        products = self.driver.find_elements(By.CSS_SELECTOR, '.productinfo.text-center p')
        for product in products:
            product_name = product.text.lower()  
            assert 'dress' in product_name, f"Product name '{product_name}' does not contain 'saree'."

        print(f"All {len(products)} products contain the word 'saree' in their name.")


    def test_add_review_without_email(self):
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        self.driver.find_element(By.ID, "name").click()
        self.driver.find_element(By.ID, "name").send_keys("sabeel")
        self.driver.find_element(By.ID, "review").send_keys("great product")
        self.driver.find_element(By.ID, "button-review").click()
        #print(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#email[name='username']"))).get_attribute("validationMessage"))
        msg = self.driver.find_element(By.ID, "email")
        validation_message = msg.get_attribute("validationMessage")
        assert validation_message == "Please fill out this field."

    