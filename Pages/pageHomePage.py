from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locatorsHomePage import *

class pageHomePage():
  
  def __init__(self, driver):
    self.driver = driver
    
    self.elements_button_css          = locatorsHomePage.elements_button_css


  def click_elements(self):
      self.driver.find_element(By.CSS_SELECTOR, self.elements_button_css).click()