import pytest
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestCheckout():
    def setup_method(self):
        service=ChromeService(ChromeDriverManager().install())
        self.driver=webdriver.Chrome(service=service)
        #self.driver=webdriver.Edge()
        self.download_folder = "C:\\Users\\Sabeel Elbedour\\Downloads"  # Set to your Downloads folder

        # Set Chrome options to set download directory
        chrome_options = webdriver.ChromeOptions()
        prefs = {"download.default_directory": self.download_folder,
                 "download.prompt_for_download": False,  
                 "download.directory_upgrade": True,
                 "safebrowsing.enabled": True  }  
        chrome_options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        

        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("sa@qa")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("sabeel")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        time.sleep(1)

    def test_checkout_login_alert(self):
        self.driver.execute_script("window.scrollTo(0,310)")
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".cart")))
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()        
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(1)").text == "Register / Login account to proceed on checkout."
  
    def test_checkout_page_after_login(self):
        self.login()
        self.driver.execute_script("window.scrollTo(0,308)")
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".step-one:nth-child(2) > .heading").is_displayed()

    def test_login_after_checkout(self):
        self.driver.execute_script("window.scrollTo(0,308)")
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "a:nth-child(1) > u")))
        self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > u").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME,"email")))
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("sa@qa")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("sabeel")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".step-one:nth-child(2) > .heading").is_displayed()

    def test_place_order(self):
        self.login()
        self.driver.execute_script("window.scrollTo(0,310)")
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".cart")))
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()        
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
        #self.driver.execute_script("window.scrollTo(0,308)")
        element=self.driver.find_element(By.LINK_TEXT, "Place Order")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name_on_card")))
        self.driver.find_element(By.NAME, "name_on_card").click()
        self.driver.find_element(By.NAME, "name_on_card").send_keys("sabeel")
        self.driver.find_element(By.NAME, "card_number").click()
        self.driver.find_element(By.NAME, "card_number").send_keys("123456")
        self.driver.find_element(By.NAME, "cvc").click()
        self.driver.find_element(By.NAME, "cvc").send_keys("123")
        self.driver.find_element(By.NAME, "expiry_month").click()
        self.driver.find_element(By.NAME, "expiry_month").send_keys("12")
        self.driver.find_element(By.NAME, "expiry_year").click()
        self.driver.find_element(By.NAME, "expiry_year").send_keys("1234")
        self.driver.find_element(By.ID, "submit").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "b:nth-child(1)")))
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, "b:nth-child(1)").text=="ORDER PLACED!"
  

    def test_address_details(self):
        self.login()
        self.driver.execute_script("window.scrollTo(0,310)")
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".cart")))
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()        
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "#address_delivery > .address_firstname").text=="Mrs. sabeel qa"
        
    def test_is_cart_empty_after_checkout(self):
        self.login()
        self.driver.execute_script("window.scrollTo(0,310)")
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".cart")))
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()        
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
        #self.driver.execute_script("window.scrollTo(0,308)")
        element=self.driver.find_element(By.LINK_TEXT, "Place Order")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name_on_card")))
        self.driver.find_element(By.NAME, "name_on_card").click()
        self.driver.find_element(By.NAME, "name_on_card").send_keys("sabeel")
        self.driver.find_element(By.NAME, "card_number").click()
        self.driver.find_element(By.NAME, "card_number").send_keys("123456")
        self.driver.find_element(By.NAME, "cvc").click()
        self.driver.find_element(By.NAME, "cvc").send_keys("123")
        self.driver.find_element(By.NAME, "expiry_month").click()
        self.driver.find_element(By.NAME, "expiry_month").send_keys("12")
        self.driver.find_element(By.NAME, "expiry_year").click()
        self.driver.find_element(By.NAME, "expiry_year").send_keys("1234")
        self.driver.find_element(By.ID, "submit").click()
        self.driver.find_element(By.LINK_TEXT, "Cart").click()
        assert self.driver.find_element(By.CSS_SELECTOR,"#empty_cart > p > b").text==" Cart is empty!"


    def test_invoice_download(self):
        self.login()
        self.driver.execute_script("window.scrollTo(0,310)")
        self.driver.find_element(By.LINK_TEXT, "View Product").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".cart")))
        self.driver.find_element(By.CSS_SELECTOR, ".cart").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "u").click()        
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
        element=self.driver.find_element(By.LINK_TEXT, "Place Order")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name_on_card")))
        self.driver.find_element(By.NAME, "name_on_card").click()
        self.driver.find_element(By.NAME, "name_on_card").send_keys("sabeel")
        self.driver.find_element(By.NAME, "card_number").click()
        self.driver.find_element(By.NAME, "card_number").send_keys("123456")
        self.driver.find_element(By.NAME, "cvc").click()
        self.driver.find_element(By.NAME, "cvc").send_keys("123")
        self.driver.find_element(By.NAME, "expiry_month").click()
        self.driver.find_element(By.NAME, "expiry_month").send_keys("12")
        self.driver.find_element(By.NAME, "expiry_year").click()
        self.driver.find_element(By.NAME, "expiry_year").send_keys("1234")
        self.driver.find_element(By.ID, "submit").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "b:nth-child(1)")))
        download_button =self.driver.find_element(By.LINK_TEXT,"Download Invoice")
        actions = ActionChains(self.driver)
        actions.move_to_element(download_button).click().perform()

        time.sleep(10)
        downloaded_files=os.listdir(self.download_folder)
        file_name="invoice.txt"
        assert file_name in downloaded_files, f"Expected file {file_name} not found in download folder"
