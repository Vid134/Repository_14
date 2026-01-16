import time     ##imports python's built in time module
from pages.login_page import LoginPage   ##imports the login page class
from pages.dashboard_page import DashboardPage   ##imports the dashboard behaviour after login

##Defines a test case named test_succesful_login
##browser context is a fixture provided by playwright to give a browser page object
def test_successful_login(browser_context):
    page = browser_context          ##to create a local variable page so we can use it everywhere we need
    login = LoginPage(page)         ##creates login page object and the browser page tpo login action happens
    dashboard = DashboardPage(page)   ##acreates the dashboard page object to check dashboard elements on that page

    login.load("https://v2.zenclass.in/login")  ##opens the specified login url
    login.enter_username("vidhya.venkruk@gmail.com")   ##giving the  username to the input box
    login.enter_password("Ganesha@2021")                ##giving the  password to the input box
    login.click_login()                                 ##clicks the login button to perform the login operation

    assert dashboard.is_dashboard_loaded() == True   ##verifies the login is succesful by checking if the
                                                           ##dashboard is visible



