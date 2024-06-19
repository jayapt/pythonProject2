
#Main menu validation on Admin page

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
            assert (self.driver.current_url == self.dashboard)
            print("Successfully logged into the webpage of OrangeHRM")
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().AdminLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().PimLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().LeaveLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().TimeLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().RecruitmentLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().My_InfoLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().PerformanceLocator)
            locator.WebLocators().clickbutton(self.driver, locator.WebLocators().DashboardLocator)
            #locator.WebLocators().clickbutton(self.driver, locator.WebLocators().MaintenanceLocator)
            #locator.WebLocators().clickbutton(self.driver, locator.WebLocators().BuzzLocator)

            # Validate Menu options on the admin page
            menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment","My Info", "Performance", "Dashboard", "Maintenance", "Buzz"]
            for option in menu_options:
                try:
                    self.driver.find_element_by_link_text(option)

                except:
                    print(f"{option} option is  displayed.")
        except NoSuchElementException as e:
            print("error")