from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.pageElements import page
import unittest
import HtmlTestRunner
import time

class demoqaElements(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(executable_path= r"C:\Program Files\Python310\Chome_Driver\chromedriver.exe")
    cls.driver.maximize_window()
  
  def test_elements(self):
    driver = self.driver
    driver.get("https://demoqa.com/elements")
    time.sleep(3)
    
    testCase = page(driver)
    testCase.click_textbox()
    time.sleep(3)
    testCase.enter_username("Edwin Tovar")
    time.sleep(3)



  @classmethod  
  def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
    time.sleep(3)
    print("Test Completado")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\Edwin Tovar\Desktop\DemoQA\reportes"))
