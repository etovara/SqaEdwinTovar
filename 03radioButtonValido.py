from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import *
from selenium.webdriver.support import expected_conditions as EC
from Pages.pageElements import pageElementsRadioButton
import unittest
import HtmlTestRunner
import time

class demoqaElements(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path= r"C:\Program Files\Python310\Chome_Driver\chromedriver.exe")
    cls.driver.maximize_window()
  
  def test_elements_RadioButton(self):
    driver = self.driver
    driver.get("https://demoqa.com/radio-button")
    
    testCaseElementsRadioButton = pageElementsRadioButton(driver)
    testCaseElementsRadioButton.yesRadio()
    time.sleep(2)
    testCaseElementsRadioButton.impressiveRadio()
    time.sleep(2)

  @classmethod  
  def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
    time.sleep(3)
    print("Test Completado")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\Edwin Tovar\Desktop\DemoQA\reportes"))