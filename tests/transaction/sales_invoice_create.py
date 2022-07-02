from pages.transaction.sales_invoice_page import SalesInvoice
import unittest
import pytest
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.si = SalesInvoice(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(1)
    def test_validLogin(self):
        # self.lp.login("ivyadmin","ivypass")
        self.si.login("dhivbranch", "1")

    def sales_invoice_create(self):
        self.si.clickDMSSales().click()
        self.si.webScroll()
        self.si.clickDMSInvoice()
        self.si.clickInvoiceCreate()
        #self.driver.switch_to.frame(0)


