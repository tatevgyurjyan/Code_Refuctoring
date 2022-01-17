from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import logging
import pytest


logging.basicConfig(filename='test_log.txt',
                    filemode='a+',
                    format='%(created)f - %(levelname)s - %(message)s',
                    level=logging.INFO
                    )


def logger(msg="", error=False):

    if error:
        logging.error(msg)
    else:
        logging.info(msg)


@pytest.fixture
def driver():
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        yield driver
        driver.quit()
    except Exception as e:
        raise Exception(e)
