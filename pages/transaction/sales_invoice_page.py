import utilities.custom_logger as cl
import logging
from base.basepage import BasePage

class SalesInvoice(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _username = "UserName"
    _password = "Password"
    _login = "Login"
    _dms_sales = "a[title='DMS Sales']"
    _dms_invoice = "a[title='Sales Invoice']"
    _dms_invoice_create = "a[title='Sales Invoice Create']"

    def enterUserName(self, username):
        self.sendKeys(username, self._username)

    def enterPassword(self, password):
        self.sendKeys(password, self._password)

    def clickLogin(self):
        self.elementClick(self._login)

    def clearFields(self):
        userField = self.getElement(locator=self._username)
        userField.clear()
        passField = self.getElement(locator=self._password)
        passField.clear()

    def login(self, username="", password=""):
        #self.clearFields()
        self.enterUserName(username)
        self.enterPassword(password)
        self.clickLogin()

    def clickDMSSales(self):
        self.elementClick(locator=self._dms_sales,locatorType="css")

    def clickDMSInvoice(self):
        self.elementClick(locator=self._dms_invoice,locatorType="css")

    def clickInvoiceCreate(self):
        self.elementClick(locator=self._dms_invoice_create,locatorType="css")


