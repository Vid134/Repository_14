from playwright.sync_api import Page, expect    ##imports playwright objects i.e page and expect

##Defines a page object model class for login actions and locators
class LoginPage:
    ##this  method runs automatically when creating the class
    def __init__(self, page: Page):
        self.page = page      #Stores the browser page inside the class so other functions can use it
        self.username_input = page.get_by_placeholder("Enter your mail")   ##locator for the username field
        self.password_input = page.get_by_placeholder("Enter your password ")   ##locator for the password field
        self.login_button = page.locator('button[type="submit"]')     ##locator for the login button
        self.error_message = page.locator("p.MuiFormHelperText-root")    ##locator of the error message popup
        self.email_error = self.error_message.nth(0)           ##error message fon email username not filled
        self.password_error = self.error_message.nth(1)            ##error message for password box not filled

## Defines a function named load which takes url as argument
    def load(self, url):
        ##try block to catch any errors while loading page
        try:
            self.page.goto(url)    ##tells playwright to navigate the browser to the given url
        except Exception as e:    ##if any error happens during page load , this will catch it
            raise Exception("Failed to load login page") from e      ##throws a clear custom error instead of a confusing default error

##Defines a method to type into the username field
    def enter_username(self, username):
        try:
            ##Try block so that if field is missing, it wont break silently
            expect(self.username_input).to_be_visible()    ##waits until the username input field is visible on the ui
            self.username_input.fill(username)         ##Types the provided username into the username field
        except Exception as e:                   ##shows up problems like element not found or not visible
            raise Exception("Username field not usable") from e     ##Raises a friendly message if username cannot be typed

##Defines a method to fill the password input field
    def enter_password(self, password):
        try:     ##try block usage
            expect(self.password_input).to_be_visible()    ##waits until password box is visible before typing
            self.password_input.fill(password)             ##types password into password field
        except Exception as e:                         ##catches runtime errors while typing password
            raise Exception("Password field not usable") from e   ##shows meaningful error message if fails

##Defines method to click login button
    def click_login(self):
        try:  ##try block usage to avoid errors
            expect(self.login_button).to_be_enabled()    ##Checks that the login button is clickable
            self.login_button.click()     ##clicks the login button
        except Exception as e:     ##catches failure cases
            raise Exception("Login button not clickable") from e    ##raises a clean error to the tester

##Defines a method to read the login error message
    def get_error_message(self):
        return self.error_message.inner_text()
     ##Returns the visible text inside the error message element

