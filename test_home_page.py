import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


#from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

#options=ChromeOptions()
#options.set_capability("browserName","chrome")
#options.set_capability("browserVersion","latest")
#options.set_capability("platformName","Windows")

#driver=webdriver.Remote("http://localhost:4444/wd/hub",options=options)


class TestHomePage():
    def setup_method(self):
        service=ChromeService(ChromeDriverManager().install())
        self.driver=webdriver.Chrome()
        #self.driver=webdriver.Edge()

        self.driver.get("https://automationexercise.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
    
    @pytest.mark.skip
    def test_carousel(self):
        #self.driver.find_element(By.CSS_SELECTOR, ".control-carousel > .fa-angle-right").click()
        #time.sleep(6)
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".active .girl")))
        ##img1=self.driver.find_element(By.CSS_SELECTOR,"#slider-carousel > div > div:nth-child(2) > div:nth-child(2) > img")
        time.sleep(4)
        #img2=self.driver.find_element(By.CSS_SELECTOR,"#slider-carousel > div > div.item.active > div:nth-child(2) > img")
        self.driver.close()


    def test_scrollUpButton(self):
        self.driver.execute_script("window.scrollTo(0,309.6000061035156)")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-angle-up").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".logo > a > img")
        assert element.is_displayed()

    def test_subscription(self):
        self.driver.execute_script("window.scrollTo(0,6000)")
        self.driver.find_element(By.CSS_SELECTOR, ".single-widget > h2").click()
        self.driver.find_element(By.ID, "susbscribe_email").click()
        self.driver.find_element(By.ID, "susbscribe_email").send_keys("a2@1")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-arrow-circle-o-right").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".alert-success").text == "You have been successfully subscribed!"

    def test_category(self):
        self.driver.execute_script("window.scrollTo(0,310)")
        self.driver. find_element(By.CSS_SELECTOR, ".panel:nth-child(1) > .panel-heading a").click()
        WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#Women li:nth-child(1) > a")))
        self.driver.find_element(By.CSS_SELECTOR, "#Women li:nth-child(1) > a").click()
        time.sleep(1)
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "WOMEN - DRESS PRODUCTS"
  

    def test_carousel_item_transition(self):
        # Locate the carousel and the item groups inside
        carousel = self.driver.find_element(By.ID, "recommended-item-carousel")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", carousel)
        carousel_items = self.driver.find_elements(By.CSS_SELECTOR, ".carousel-inner .item")
        
        # Find the initial active group
        initial_active_group = None
        for item in carousel_items:
            if "active" in item.get_attribute("class"):
                initial_active_group = item
                break

        assert initial_active_group is not None, "No active group found initially!"

        # Wait for the carousel to change (either automatically or manually by clicking next)
        #next_button = self.driver.find_element(By.CSS_SELECTOR, '.right.recommended-item-control')
        #next_button.click()

        # Optionally, wait for the carousel to change
        time.sleep(5)

        # Find the new active group
        new_active_group = None
        for item in carousel_items:
            if "active" in item.get_attribute("class"):
                new_active_group = item
                break

        # Verify that the active group has changed
        assert new_active_group != initial_active_group, "Carousel did not change the active group!"

        