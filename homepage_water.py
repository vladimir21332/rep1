from water_rmv.base_water_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By



class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



# open homepage

    def open(self):
        self.driver.get("https://www.smwd.com/")

    @property
    def pay_my_bill(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="graphicLinkWidget9073275e-9d1d-479c-83ac-543a910893ed"]/div[2]/div/div[1]/div/div/div/a')))


    def text(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pay-my-bill"]/h2'))).text

    def sign_pay_now(self):
        return self.driver.find_element_by_xpath('//*[@id="headingOne"]/a/span')

    def sign_pay_now_color(self):
        return self.driver.value_of_css_property('color-paybill ')






    def all_homepege(self):
        self.pay_my_bill.click()

