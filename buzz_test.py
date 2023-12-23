import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_post_to_buzz(driver):
    driver.get("http://localhost/OrangeHRM/web/index.php/auth/login")
    
    id = driver.find_element('xpath', '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    password = driver.find_element('xpath', '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
    submit = driver.find_element('xpath', '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button') 
    
    id.send_keys('admin@admin.com')
    password.send_keys('SQA@admin123')
    submit.click()
    time.sleep(3)

    buzz = driver.find_element('xpath', '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a/span') 
    buzz.click()
    time.sleep(5)

    post = driver.find_element('xpath', '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/form/div/textarea') 
    post.send_keys('hello this is my first post')
    submit = driver.find_element('xpath', '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/form/div/div/button') 
    submit.click()
    assert "pytest" in driver.page_source
    time.sleep(5)
driver()
test_post_to_buzz(driver)