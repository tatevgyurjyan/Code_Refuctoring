from selenium.webdriver.common.by import By
from Helper import helpers
import conftest
import json


sign_in = (By.XPATH,
           "//section[@class='header__user-menu']//a[@href='/users/sign_in']")
create_acc_link = (By.XPATH, "//a[contains(text(), 'new account')]")
txt_fname = (By.XPATH, "//input[@id='user[first_name]']")
txt_lname = (By.XPATH, "//input[@id='user[last_name]']")
txt_email = (By.XPATH, "//input[@id='user[email]']")
txt_pswd = (By.XPATH, "//input[@id='user[password]']")
chbox_terms_of_use = (By.XPATH, "//input[@id='user[terms]']")
sign_up_btn = (By.XPATH, "//input[@value='Sign up']")
user_account_name = (By.XPATH, "//a[@class='dropdown__toggle-button']")


with open("/home/tatevik/Desktop/QA/Final/Testdata/config.json") as f:
    data = json.load(f)


def registration(driver):
    try:
        data['email'] = helpers.email_generator(driver)
        data['pswd'] = helpers.password_generator(driver)
        helpers.find_and_click(driver, sign_in)
        helpers.find_and_click(driver, create_acc_link)
        helpers.find_and_send_keys(driver, txt_fname, data['fname'])
        helpers.find_and_send_keys(driver, txt_lname, data['lname'])
        helpers.find_and_send_keys(driver, txt_email, data['email'])
        helpers.find_and_send_keys(driver, txt_pswd,  data['pswd'])
        helpers.find_and_click(driver, chbox_terms_of_use)
        helpers.find_and_click(driver, sign_up_btn)
        greetings_txt = helpers.find(driver, user_account_name)
        with open(
                "/home/tatevik/Desktop/QA/Final/Testdata/config.json",
                "w") as f:
            json.dump(data, f)
        conftest.logger(f"User's name is {greetings_txt.text}")
        conftest.logger(f"Generated email is {data['email']}")
        conftest.logger(f"Generated password is {data['pswd']}")
    except Exception as e:
        conftest.logger(e)
