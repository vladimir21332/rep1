from selenium import webdriver
import pytest
import time
from pytest import mark
from webdriver_manager.chrome import ChromeDriverManager

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

    @pytest.mark.ui
    def test_google_page_2(self, test_setup):
        driver.maximize_window()
        driver.get("https://amazon.com/")
        time.sleep(1)
