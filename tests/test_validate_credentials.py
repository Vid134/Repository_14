from pages.login_page import LoginPage   ##imports the login page class to interact with the login screen using the pom
from playwright.sync_api import expect   ##imports expect which allows us to write assertions

##defines the test case named test_validate_input_boxes
##browser context is a fixture provided by playwright to give a browser page object
def test_validate_input_boxes(browser_context):
    page = browser_context                 ####to create a local variable page so we can use it everywhere we need
    login = LoginPage(page)                ####creates login page object and the browser page tpo login action happens

    # Load login page
    login.load("https://v2.zenclass.in/login")

    # Validate Username field is visible & enabled
    expect(login.username_input).to_be_visible()
    expect(login.username_input).to_be_enabled()

    # Validate Password field is visible & enabled
    expect(login.password_input).to_be_visible()
    expect(login.password_input).to_be_enabled()
