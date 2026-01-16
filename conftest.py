import pytest           ##Imports the pytest library so we can create fixtures and run tests
from playwright.sync_api import sync_playwright   ##Imports playwrights sync api runner so we can automate browser actions

##this decorator tells pytest that the function below is a fixture
##fixture allow test functions to reuse browser setup easily
@pytest.fixture()
##Defines the fixture function called browser context
def browser_context():
    with sync_playwright() as p:  ##starts the playwright engine in sync mode, the with block ensures playwright closes properly after tests
        browser = p.chromium.launch(headless=False)   ##launches a chromium browser instance,headless=false means browser ui is visible
        context = browser.new_context()   ##creates a new browser context,wont share cookies and storage
        page = context.new_page()          ##opens a new page inside that context
        yield page                          ##yield returns the page to the test that requested this fixture,after the test finish, code after yield will run
        context.close()      ## Closes the browser context after test completes
        browser.close()      ##shutsdown the entire browser to free resources