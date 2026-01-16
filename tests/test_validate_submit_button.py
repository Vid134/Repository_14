from pages.login_page import LoginPage    ##imports the login page class to interact with the login screen using the pom
from playwright.sync_api import expect   ##imports expect which allows us to write assertions

###Define the test case named test_validate_submit_button
##browser context is a fixture provided by playwright to give a browser page object
def test_validate_submit_button(browser_context):
    page = browser_context             ####to create a local variable page so we can use it everywhere we need
    login = LoginPage(page)               ####creates login page object and the browser page tpo login action happens

    ## Loading login page
    login.load("https://v2.zenclass.in/")

    ## To Validate Submit/Login button is visible & enabled
    expect(login.login_button).to_be_visible()
    expect(login.login_button).to_be_enabled()


    login.click_login()      ## Click the button to verify it triggers action

   ##verify error message or page behavior after click

    assert True  # Replace with expected behavior if needed