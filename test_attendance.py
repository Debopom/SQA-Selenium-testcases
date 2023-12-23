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

class TestAttendance():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_attendance(self):
    self.driver.get("http://localhost/OrangeHRM/web/index.php/auth/login")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
    self.driver.find_element(By.NAME, "username").send_keys("admin@admin.com")
    self.driver.find_element(By.NAME, "password").send_keys("SQA@admin123")
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
    self.driver.find_element(By.LINK_TEXT, "Time").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Punch In/Out").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(1) .oxd-icon").click()
    self.driver.find_element(By.LINK_TEXT, "My Timesheets").click()
    self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-timesheet-table-header-row").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-layout-context").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(2) > .oxd-topbar-body-nav-tab-item").click()
    self.driver.find_element(By.LINK_TEXT, "Employee Records").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input").send_keys("Debopom  Sutradhar")
    element = self.driver.find_element(By.CSS_SELECTOR, ".oxd-form")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
  