import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import re
import time

class TestContactUs():
    def setup_method(self):
        service=ChromeService(ChromeDriverManager().install())
        self.driver=webdriver.Chrome()
        #driver=webdriver.Edge()

        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def test_invalid_email(self):
        self.driver.find_element(By.LINK_TEXT, "Contact us").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("sabeel")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("sa@")
        self.driver.find_element(By.NAME, "subject").click()
        self.driver.find_element(By.NAME, "subject").send_keys("get in touch")
        self.driver.find_element(By.ID, "message").click()
        self.driver.find_element(By.ID, "message").send_keys("hello there!")
        self.driver.find_element(By.NAME, "submit").click()
        msg = self.driver.find_element(By.NAME, "email")
        validation_message = msg.get_attribute("validationMessage")
        assert validation_message == "Please enter a part following '@'. 'sa@' is incomplete."

    def test_send_contact_details(self):
        self.driver.find_element(By.LINK_TEXT, "Contact us").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("sabeel")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("sa@qa")
        self.driver.find_element(By.NAME, "subject").click()
        self.driver.find_element(By.NAME, "subject").send_keys("get")
        self.driver.find_element(By.ID, "message").click()
        self.driver.find_element(By.ID, "message").send_keys("hello")
        self.driver.find_element(By.NAME, "submit").click()
        assert self.driver.switch_to.alert.text == "Press OK to proceed!"
        self.driver.switch_to.alert.accept()
        assert self.driver.find_element(By.CSS_SELECTOR, ".status").text == "Success! Your details have been submitted successfully."
    
    def test_home_button(self):

        self.driver.find_element(By.LINK_TEXT, "Contact us").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("sabeel")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("sa@qa")
        self.driver.find_element(By.NAME, "subject").click()
        self.driver.find_element(By.NAME, "subject").send_keys("get")
        self.driver.find_element(By.ID, "message").click()
        self.driver.find_element(By.ID, "message").send_keys("hello")
        self.driver.find_element(By.NAME, "submit").click()
        assert self.driver.switch_to.alert.text == "Press OK to proceed!"
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.CSS_SELECTOR, ".btn > span").click()
        element =self.driver.find_element(By.CSS_SELECTOR, ".control-carousel > .fa-angle-right")
        assert element.is_displayed()

    def test_titles(self):
        self.driver.find_element(By.LINK_TEXT, "Contact us").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".col-sm-12 > .title").text== "CONTACT US"
        #assert self.driver.find_element(By.CSS_SELECTOR, ".title:nth-child(2)").text== "GET IN TOUCH" 
        #assert self.driver.find_element(By.CSS_SELECTOR, ".contact-info > .title").text== "FEEDBACK FOR US" 

    def test_upload_file(self):
        self.driver.find_element(By.LINK_TEXT, "Contact us").click()
        self.driver.find_element(By.NAME, "name").click()
        self.driver.find_element(By.NAME, "name").send_keys("sabeel")
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("sa@qa")
        self.driver.find_element(By.NAME, "subject").click()
        self.driver.find_element(By.NAME, "subject").send_keys("get")
        self.driver.find_element(By.ID, "message").click()
        self.driver.find_element(By.ID, "message").send_keys("hello")
        upload=self.driver.find_element(By.CSS_SELECTOR,"input[type='file']")
        #upload.click()
        file_path="C:\\Users\Sabeel Elbedour\\Downloads\\test_file.txt"
        upload.send_keys(file_path)
        #uploaded_file_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "upload_file")))  # Replace with the actual CSS selector
        time.sleep(3)
        uploaded_file_path = upload.get_attribute("value")
        assert "test_file.txt" in uploaded_file_path, "File name does not match!"

