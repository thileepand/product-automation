import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.yield_fixture()
def setUp():
    print("Running method level setUP")
    yield
    print("Running method level teardown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("Running one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("dhivbranch", "1")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running oneTime teardown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating systems")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("osType")