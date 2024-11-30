from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.chrome.options import Options as ChromeOptions
import time

#options=ChromeOptions()
#options.set_capability("browserName","chrome")
#options.set_capability("browserVersion","latest")
#options.set_capability("platformName","Windows")

#driver=webdriver.Remote("http://localhost:4444/wd/hub",options=options)



service=ChromeService(ChromeDriverManager().install())
driver=webdriver.Chrome()
#driver=webdriver.Edge()

driver.get("https://automationexercise.com/")
driver.maximize_window()
time.sleep(3)
driver.close()

