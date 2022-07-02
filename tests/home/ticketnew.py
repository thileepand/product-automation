from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Login():
    def bookticket(self):
        baseURL = "http://www.ticketnew.com/Movie-Ticket-Online-booking/C/Chennai"
        driver = webdriver.Chrome()
        #driver = webdriver.Firefox(executable_path="/home/nadmin/Documents/driver/geckodriver")
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        element1 = driver.find_element(By.ID, "nav-link-theatres")

        itemToLocator = ".//*[@id='nav']//a[text()='Sangam Cinemas']"

        action = ActionChains(driver)
        action.move_to_element(element1).click().perform()
        print("Mouse Hovered on Element")
        time.sleep(2)
        toplink = driver.find_element(By.XPATH, itemToLocator)
        time.sleep(2)

        action.move_to_element(toplink).click().perform()
        print("Theater selected")

        dateselect = driver.find_element(By.XPATH, ".//*[@id='divDates']//span[text()='1']")
        dateselect.click()
        print("Date selected")
        time.sleep(3)

        movie = driver.find_element(By.XPATH, ".//*[@id='movie-name-list']//a[text()='Kavan (U) - Tamil']")
        movie.click()

        seat = driver.find_element(By.XPATH, ".//span[@class='faux-select-right png_bg']")
        seat.click()
        time.sleep(2)

        selectperson = driver.find_element(By.XPATH, ".//*[@id='faux-select-overlay-overflowed-content']//a[text()='2']")
        selectperson.click()

        showtime = driver.find_element(By.XPATH, ".//*[@id='tblClassdetails']/tbody/tr[6]/td[5]/ul/li[1]/a")
        showtime.click()
        time.sleep(3)
        print("Time selected")

        selectseat = driver.find_element(By.XPATH, ".//td[@id='s_7']")
        selectseat.click()
        print("seat selected")
        time.sleep(3)

        payment = driver.find_element(By.XPATH, ".//*[@id='content-without-sidebar-container']//span[text()='Proceed to pay']")
        payment.click()
        print("Payment generated")
        time.sleep(5)


ff = Login()
ff.bookticket()