from pages.login_page import LoginPage   ##imports the login page class to interact with login fields

##Defines a test case named test_unsuccesful_login
##browser context is a fixture provided by playwright to give a browser page object
def test_unsuccessful_login(browser_context):
    page = browser_context      ####to create a local variable page so we can use it everywhere we need
    login = LoginPage(page)      ####creates login page object and the browser page tpo login action happens

    login.load("https://v2.zenclass.in/login")    ##opens the specified login url
    login.enter_username("wrongUser")              ##entering the wrong username
    login.enter_password("wrongPass")               #3entering the wrong password
    login.click_login()                             ##to click the login button

    assert login.get_error_message() != ""           ##After login fails this line checks that an error message apppears
