# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestInvalidLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_invalidLogin(self):
    self.driver.get("http://localhost/OrangeHRM/web/index.php/auth/login")
    self.driver.set_window_size(974, 528)
    self.driver.find_element(By.NAME, "username").send_keys("admin@addsa")
    self.driver.find_element(By.NAME, "password").send_keys("SQA@admin123")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
  
