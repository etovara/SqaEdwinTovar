from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import *
from selenium.webdriver.support import expected_conditions as EC
from Pages.pageElements import *
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
    driver.get("https://www.online-notepad.net/es/bloc-de-notas-online")
    
    testBase = pagesElements(driver)
    testBase.click_textbox()
    time.sleep(2)
   
  def testTarea(self):
    driver = self.driver
    driver.get("https://www.online-notepad.net/es/bloc-de-notas-online")
        
    testTarea = pagesTarea(driver)
    testTarea.click_tarea()
    time.sleep(2)
    testTarea.enter_input("Prueba01")

  @classmethod  
  def tearDownClass(cls):
    cls.driver.close()
    cls.driver.quit()
    time.sleep(3)
    print("Test Completado")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\Edwin Tovar\Desktop\Base\reportes"))