import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture
def driver():
    driver = webdriver.Chrome(ChromeDriverManager().install)
    driver.maximize_window()
    driver.quit()
    return driver
    
    


