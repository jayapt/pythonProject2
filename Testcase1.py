#Forgot Password link validation on login page


from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest


class Test:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture
    @pytest.fixture
    def boot(self):
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # implementation of implicit wait
        self.driver.implicitly_wait(10)
        yield

        self.driver.quit()

    # pytest html file
    @pytest.mark.html
    def test_login(self, boot):
        try:
            self.driver.get(data.WebData().url)
            self.driver.maximize_window()
            locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().forgotLocator)
            locator.WebLocators().x_path(self.driver, locator.WebLocators().username_Locator, data.WebData().username)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().reset_Locator)
            print("successful : A reset password link has been sent to you via email.")
        except NoSuchElementException as e:
             print("error")
