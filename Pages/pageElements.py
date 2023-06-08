from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locatorsElements import *

class pagesElements():
  
  def __init__(self, driver):
    self.driver = driver
    
    self.click_textbox_id          = locatorsElements.click_textbox_id


      
  def click_textbox(self):
    self.driver.find_element(By.XPATH, self.click_textbox_id).click()
  

    
class pagesTarea():
  
  def __init__(self, driver):
    self.driver = driver
  
    self.list_tarea_xpath                =  tarea.click_tarea
    self.enter_input                     = tarea.text_input
  
  def click_tarea(self):
    self.driver.find_element(By.XPATH, self.list_tarea_xpath).click()
  
  def enter_text(self, text):
    self.driver.find_element(By.ID, self.text_input).send_keys(text)