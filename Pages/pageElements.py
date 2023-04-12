from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from Locators.locatorsElements import *

class pageElementsTextBox():
  
  def __init__(self, driver):
    self.driver = driver
    
    self.click_textbox_xpath          = locatorsElements.click_textbox_xpath
    self.userName_textbox_id          = locatorsElements.userName_textbox_id
    self.email_textbox_id             = locatorsElements.email_textbox_id
    self.currentAddress_textbox_id    = locatorsElements.currentAddress_textbox_id
    self.permanentAddress_textbox_id  = locatorsElements.permanentAddress_textbox_id
    self.submit_button_id             = locatorsElements.submit_button_id
      
  def click_textbox(self):
    self.driver.find_element(By.XPATH, self.click_textbox_xpath).click()
  
  def enter_username(self, userName):
    self.driver.find_element(By.ID, self.userName_textbox_id).clear()
    self.driver.find_element(By.ID, self.userName_textbox_id).send_keys(userName)
  
  def enter_email(self, email):
    self.driver.find_element(By.ID, self.email_textbox_id).clear()
    self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)
  
  def enter_currentAddress(self, currentAddress):
    self.driver.find_element(By.ID, self.currentAddress_textbox_id).clear()
    self.driver.find_element(By.ID, self.currentAddress_textbox_id).send_keys(currentAddress)
    
  def enter_permanentAddress(self, permanentAddress):
      self.driver.find_element(By.ID, self.permanentAddress_textbox_id).clear()
      self.driver.find_element(By.ID, self.permanentAddress_textbox_id).send_keys(permanentAddress)
      

      
  def enter_submit(self, submit):
      self.driver.find_element(By.ID, self.submit_button_id).clear()
      self.driver.find_element(By.ID, self.submit_button_id).send_keys(submit)
      ActionChains(self).scroll_to_element(self.enter_submit)

class pageElementsCheckBox():
      
  def __init__(self, driver):
    self.driver = driver
    
    self.checkbox_button_xpath          = locatorsElementsCheckBox.checkbox_button_xpath

      
  def checkbox_button(self):
    self.driver.find_element(By.XPATH, self.checkbox_button_xpath).click()