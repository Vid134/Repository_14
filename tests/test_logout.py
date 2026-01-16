from pages.login_page import LoginPage    ##imports the login page class to interact with login fields
from pages.dashboard_page import DashboardPage   ##imports the dashboard behaviour after login
from playwright.sync_api import expect            ## ##imports expect which allows us to write assertions

##Defines the test case named test_logout
##browser context is a fixture provided by playwright to give a browser page object
def test_logout(browser_context):
    page = browser_context     ##to create a local variable page so we can use it everywhere we need
    login = LoginPage(page)     ##creates login page object and the browser page to login action happens
    dashboard = DashboardPage(page)   ##to create dashboard page object to handle dashboard specific elements

    login.load("https://v2.zenclass.in/login")   #opens the specified login url
    login.enter_username("vidhya.venkruk@gmail.com")    ##entering the right username
    login.enter_password("Ganesha@2021")                  #3entering the right password
    login.click_login()                                   ##to click login button
    page.wait_for_load_state("networkidle")          ##waits until the network has been idle adn the page is loaded well

    assert dashboard.is_dashboard_loaded() == True    ##validation method to verify the dashboard has loaded,if true it passes
    dashboard.click_logout()                            ##calls the logout method from dashboard page by clicking the avatar icon for logout

    page.wait_for_url("**/login",timeout=5000)       ##waits until the current url matches the login page
                                                  ##timeout = 5000 means waiting upto 5 seconds


    #final validation that confirms the logout succeeded
    expect(login.username_input).to_be_visible()