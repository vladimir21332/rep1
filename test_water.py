import pytest
from selenium import webdriver
import time
import allure

from pytest import mark
from water_rmv.homepage_water import HomePage
from water_rmv.landing_water_page import LandingPage
from webdriver_manager.chrome import ChromeDriverManager


# @mark.smoke
class TestLandingPage:
    @pytest.fixture()
    def test_setup(self):
        global driver

        # driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # this is time wait before driver quite (browser close)

        yield
        time.sleep(2)
        driver.quit()

    # @mark.ui
    # @allure.description("test sample 1")
    # @allure.severity(severity_level='CRITICAL')
    def test_sign_in_flow(self, test_setup):
        driver.maximize_window()
        landing_page = LandingPage(driver)
        landing_page.open()
        landing_page.all_sign_in()
        #driver.save_screenshot("screenshot.png")
        time.sleep(2)
        text = landing_page.text()
        try:
            assert text == '$93.34'
        finally:
            if (AssertionError):
                allure.attach(driver.get_screenshot_as_png(),name='invalin price',attachment_type=allure.attachment_type.PNG)

        text2 = landing_page.text2()
        assert text2 == '00579605'
        assert 'https://il.smwd.com/' in driver.current_url


    # @mark.skip(reason="needs to be fixed")
    # @allure.description("test sample 2")
    # @allure.severity(severity_level='NORMAL')
    def test_homepage(self,test_setup):
        driver.maximize_window()
        homepage = HomePage(driver)
        homepage.open()
        homepage.all_homepege()
        text = homepage.text()
        assert text == 'One-Time Payment'
        sign = homepage.sign_pay_now()
        color = sign.value_of_css_property('background-color')
        assert color == 'rgba(255, 255, 255, 1)'



