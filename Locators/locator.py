#Locators for Pytest

from selenium.webdriver.common.by import By

class WebLocators:
    usernameLocator = "username"
    passwordLocator = "password"
    buttonLocator = "//button[@type='submit']"
    emp_fn_Locator = "//input[@name='firstName']"
    emp_ln_locator = "//input[@name='lastName']"
    emp_id_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    addLocator = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']"
    saveLocator = "//button[@type='submit']"
    editLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[10]/div/div[9]/div/button[2]'
    deleteLocator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[18]/div/div[9]/div/button[1]'
    yesbuttonLocator = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
    forgotLocator = "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    username_Locator = "//input[@class='oxd-input oxd-input--active']"
    reset_Locator = "//button[@type='submit']"

    User_ManagementLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]'
    JobLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]'
    OrganizationLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]'
    QualificationsLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]'
    NationalitiesLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]'
    Corporate_BankingLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]'
    ConfigurationLocator = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span'


    #adminLocator = "//a[@class='oxd-main-menu-item active']"
    AdminLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'
    PimLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    LeaveLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a'
    TimeLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a'
    RecruitmentLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a'
    My_InfoLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a'
    PerformanceLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a'
    DashboardLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a'
    DirectoryLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a'
    MaintenanceLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a'
   # BuzzLocator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'

    def entertext(self, driver, locator, textvalue):
         driver.find_element(by=By.NAME, value=locator).send_keys(textvalue)

    def clickbutton(self, driver, locator):
         driver.find_element(by=By.XPATH, value=locator).click()

    def link_text(self, driver, locator):
         driver.find_element(by=By.LINK_TEXT, value=locator).click()

    def x_path(self, driver, locator, textvalue):
         driver.find_element(by=By.XPATH, value=locator).send_keys(textvalue)

