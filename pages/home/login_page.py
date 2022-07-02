import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _username = "UserName"
    _password = "Password"
    _login = "Login"
    _home_page = "//h2[contains(text(),'Welcome To Cloud DMS')]"
    _invalid_login = "//div[contains(text(), 'Invalid User Name Or Password.')]"
    _logout_icon = "prof-anchor"
    _logout = "a[title='Logout']"


    def enterUserName(self, username):
        self.sendKeys(username, self._username)

    def enterPassword(self, password):
        self.sendKeys(password, self._password)

    def clickLogin(self):
        self.elementClick(self._login)

    def login(self, username="", password=""):
        self.clearFields()
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLogin()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self._home_page, locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(self._invalid_login, locatorType="xpath")
        return result

    def clearFields(self):
        userField = self.getElement(locator=self._username)
        userField.clear()
        passField = self.getElement(locator=self._password)
        passField.clear()

    def verifyLoginTitle(self):
        return self.verifyPageTitle("IvyDMS")

    def logout(self):
        self.elementClick(self._logout_icon)
        self.elementClick(self._logout,locatorType="css")




