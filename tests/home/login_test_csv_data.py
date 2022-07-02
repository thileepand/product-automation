from pages.home.login_page import LoginPage
import unittest
import pytest
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@ddt
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTestWithCSVData(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(2)

    def test_validLogin(self):
           #self.lp.login("ivyadmin","ivypass")
           self.lp.login("ivyadmin", "SupPass")
           self.driver.switch_to.frame(0)
           result1 = self.lp.verifyLoginTitle()
           self.ts.mark(result1, "Title is incorrect")
           assert result1 == True
           result2 = self.lp.verifyLoginSuccessful()
           self.ts.markFinal("test_validation", result2, "login was  successful")
           assert result2 ==True


    @pytest.mark.run(1)
    @data(*getCSVData("/home/thileepan/Documents/workspace_python/Product2/testdata.csv"))
    @unpack
    def test_invalidLogin(self, Username, Passowrd):
        self.lp.logout()
        self.lp.login(Username, Passowrd)
        result = self.lp.verifyLoginFailed()
        assert result == True




