from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Locators.locatorsElements import locatorsElements

class page():
  
  def __init__(self, driver):
    self.driver = driver
    
    self.click_textbox_xpath      = locatorsElements.click_textbox_xpath
    self.userName_textbox_id      = locatorsElements.userName_textbox_id
      
  def click_textbox(self):
    self.driver.find_element(By.XPATH, self.click_textbox_xpath).click()
  
  def enter_username(self, userName):
    self.driver.find_element(By.ID, self.userName_textbox_id).clear()
    self.driver.find_element(By.ID, self.userName_textbox_id).send_keys(userName)