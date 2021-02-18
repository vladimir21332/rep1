import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from water_rmv.base_water_page import BasePage

class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



# open landing page

    def open(self):
        self.driver.get("https://il.smwd.com/")

    @property
    def email_field(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="dnn_dnnLogin_username"]')))

    # enter username vladimir2133

    def enter_email(self):
        return self.driver.find_element_by_xpath('//*[@id="dnn_dnnLogin_username"]').send_keys("vladimir2133")

    # get password field

    @property
    def password_field(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="passworddnnLogin"]')))

    # enter password Volga2009

    def enter_password(self):
        return self.driver.find_element_by_xpath('//*[@id="passworddnnLogin"]').send_keys("Volga2009")

    # get button Log In

    @property
    def click_login_button(self):
        return self.driver.find_element_by_xpath('//*[@id="login-formdnnLogin"]/div[2]/fieldset/div/div[3]/button')


    def text(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="bill-current-balance-453"]'))).text

    def text2(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="accountList448"]/div/span[1]'))).text




# all actions for the test page


    def all_sign_in(self):
        self.email_field.click()
        self.enter_email()
        self.password_field.click()
        self.enter_password()
        self.click_login_button.click()
