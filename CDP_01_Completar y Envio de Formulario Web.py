from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import *
from selenium.webdriver.support import expected_conditions as EC
from Pages.pageElements import pagesElements
import unittest
import HtmlTestRunner
import time

class demoqaElements(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path= r"C:\Program Files\Python310\Chome_Driver\chromedriver.exe")
    cls.driver.maximize_window()
  
  
  def testBase(self):
    driver = self.driver
    driver.get("https://demoqa.com/elements")
    
    testBase = pagesElements(driver)
    testBase.click_textbox()
    time.sleep(2)    
    testBase.enter_username("Pepito Perez")
    time.sleep(2)
    testBase.enter_email("pepitoperez@pepito.com")
    time.sleep(2)
    testBase.enter_currentAddress("Ciudad Autonoma de Buenos Aires")
    time.sleep(2)
    testBase.enter_permanentAddress("Ciudad Autonoma de Buenos Aires, Argentina")
    time.sleep(2)
    testBase.enter_submit
    time.sleep(2)


  @classmethod  
  def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
    time.sleep(3)
    print("Test Completado")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\Edwin Tovar\Desktop\Base\reportes"))