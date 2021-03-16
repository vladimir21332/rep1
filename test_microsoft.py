from selenium import webdriver
import pytest
import time
from pytest import mark
from webdriver_manager.chrome import ChromeDriverManager

@mark.x
class TestAmazonPage:
    @pytest.fixture()
    def test_setup(self):
        global driver

        # driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # this is time wait before driver quite (browser close)

        yield
        time.sleep(2)
        driver.quit()

    @mark.ui
    def test_amazon_page(self, test_setup):
        driver.maximize_window()
        driver.get("https://microsoft.com/")
        time.sleep(2)