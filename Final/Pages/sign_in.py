from selenium.webdriver.common.by import By
from Helper import helpers
from Pages import sign_up
import conftest


btn_sign_in = (By.XPATH, "//input[@value='Sign in']")


def login_user(driver):
    try:
        if sign_up.data["email"] == '' or sign_up.data["pswd"] == '':
            sign_up.registration(driver)
        else:
            helpers.find_and_click(driver, sign_up.sign_in)
            helpers.find_and_send_keys(
                driver, sign_up.txt_email, sign_up.data['email'])
            helpers.find_and_send_keys(
                driver, sign_up.txt_pswd, sign_up.data['pswd'])
            helpers.find_and_click(driver, btn_sign_in)
            greetings_txt = helpers.find(driver, sign_up.user_account_name)
            conftest.logger(f"User's name is {greetings_txt.text}")
            conftest.logger(f"{sign_up.data['fname']} is logged in")
    except Exception as e:
        conftest.logger(e)
