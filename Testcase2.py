#Header validation on Admin Page


from Data import data
from Locators import locator
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import pytest


class Test:
    dashboard = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # pytest fixture test
    @pytest.fixture
    def boot(self, loginpage_title="OrangeHRM"):
        self.loginpage_title = loginpage_title
        # Setting up Chrome WebDriver with the WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    # pytest html files
    @pytest.mark.html
    def test_login(self, boot):
        try:
            self.driver.get(data.WebData().url)
            self.driver.maximize_window()
            locator.WebLocators().entertext(self.driver, locator.WebLocators().usernameLocator, data.WebData().username)
            locator.WebLocators().entertext(self.driver, locator.WebLocators().passwordLocator, data.WebData().password)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().buttonLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().AdminLocator)

            assert (self.driver.title == self.loginpage_title)
            print("Success:logged into the webpage of OrangeHRM")

            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().User_ManagementLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().JobLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().OrganizationLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().QualificationsLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().NationalitiesLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().Corporate_BankingLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().ConfigurationLocator)
        # Validate the admin page
            admin_options = ["User Management", "Job", "Organization", "Qualifications", "Nationalities",
                         "Corporate Branding", "Configuration"]
            for option in admin_options:
                try:
                    self.driver.find_element_by_link_text(option)

                except:
                     print(f"{option} option is  displayed.")
        except NoSuchElementException as e:
            print("error")
