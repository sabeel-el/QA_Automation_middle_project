import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestRegister():
    def setup_method(self):
        service=ChromeService(ChromeDriverManager().install())
        self.driver=webdriver.Chrome()
        #driver=webdriver.Edge()

        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()

    def test_create_new_account(self):
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name")))
        self.driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(2)").click()
        self.driver.find_element(By.NAME, "name").send_keys("sabeel2")
        self.driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(3)").send_keys("sa@qab")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.ID, "id_gender2")))
        self.driver.find_element(By.ID, "id_gender2").click()
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("sabeel")
        self.driver.find_element(By.ID, "days").click()
        dropdown = self.driver.find_element(By.ID, "days")
        dropdown.find_element(By.XPATH, "//option[. = '26']").click()
        self.driver.find_element(By.ID, "months").click()
        dropdown = self.driver.find_element(By.ID, "months")
        dropdown.find_element(By.XPATH, "//option[. = 'September']").click()
        self.driver.find_element(By.ID, "years").click()
        dropdown = self.driver.find_element(By.ID, "years")
        dropdown.find_element(By.XPATH, "//option[. = '2000']").click()
        self.driver.execute_script("window.scrollTo(0, 500)") 
        self.driver.find_element(By.ID, "newsletter").click()
        self.driver.find_element(By.ID, "first_name").click()
        self.driver.find_element(By.ID, "first_name").send_keys("sabeel")
        self.driver.find_element(By.ID, "last_name").click()
        self.driver.find_element(By.ID, "last_name").send_keys("qa")
        self.driver.execute_script("window.scrollTo(0, 800)") 
        self.driver.find_element(By.ID, "address1").click()
        self.driver.find_element(By.ID, "address1").send_keys("athar")
        self.driver.find_element(By.ID, "country").click()
        dropdown = self.driver.find_element(By.ID, "country")
        dropdown.find_element(By.XPATH, "//option[. = 'Israel']").click()
        self.driver.execute_script("window.scrollTo(0, 500)") 
        self.driver.find_element(By.ID, "state").click()
        self.driver.find_element(By.ID, "state").send_keys("athar")
        self.driver.find_element(By.ID, "city").click()
        self.driver.find_element(By.ID, "city").send_keys("rahat")
        self.driver.find_element(By.ID, "zipcode").click()
        self.driver.find_element(By.ID, "zipcode").send_keys("123")
        self.driver.find_element(By.ID, "mobile_number").click()
        self.driver.find_element(By.ID, "mobile_number").send_keys("123456789")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(22)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "b").text == "ACCOUNT CREATED!"
    

    def test_logout(self):
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "email")))
        self.driver.find_element(By.NAME,"email").click()
        self.driver.find_element(By.NAME,"email").send_keys("sa@qa")
        self.driver.find_element(By.NAME,"password").click()
        self.driver.find_element(By.NAME,"password").send_keys("sabeel")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Logout")))
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Signup / Login")))
        assert self.driver.find_element(By.LINK_TEXT, "Signup / Login").is_displayed()

    def test_delete_account(self):
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "email")))
        self.driver.find_element(By.NAME,"email").click()
        self.driver.find_element(By.NAME,"email").send_keys("sa@qab")
        self.driver.find_element(By.NAME,"password").click()
        self.driver.find_element(By.NAME,"password").send_keys("sabeel")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Delete Account")))
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Signup / Login")))
        assert self.driver.find_element(By.LINK_TEXT, "Signup / Login").is_displayed()


    def test_register_with_existing_email(self):
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name")))
        self.driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(2)").click()
        self.driver.find_element(By.NAME, "name").send_keys("person")
        self.driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(3)").send_keys("sa@qa")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
        assert self.driver.find_element(By.CSS_SELECTOR,".signup-form p").is_displayed()

    def test_register_with_empty_fields(self):
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "name")))
        self.driver.find_element(By.CSS_SELECTOR,".btn:nth-child(5)").click()
        msg = self.driver.find_element(By.NAME, "name")
        validation_message = msg.get_attribute("validationMessage")
        assert validation_message == "Please fill out this field."


    def test_login(self):
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        self.driver.find_element(By.NAME, "email").click()
        self.driver.find_element(By.NAME, "email").send_keys("sa@qa")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("sabeel")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        time.sleep(1)
        element = self.driver.find_element(By.LINK_TEXT, "Logout")
        assert element.is_displayed()


    def test_login_with_incoreect_password(self):
        self.driver.find_element(By.LINK_TEXT, "Signup / Login").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.NAME, "email")))
        em=self.driver.find_element(By.NAME, "email")
        em.click()
        em.send_keys("sa@qa")
        self.driver.find_element(By.NAME, "password").click()
        self.driver.find_element(By.NAME, "password").send_keys("123")
        self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".login-form p").text == "Your email or password is incorrect!"




        




