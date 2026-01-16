import re

from playwright.sync_api import Page, expect   ##imports playwright objects i.e page and expect

##Defines a page object model class for dashboard actions and locators
class DashboardPage:
    ##this  method runs automatically when creating the class
    def __init__(self, page: Page):
        self.page = page    ##Stores the browser page inside the class so other functions can use it
        self.dashboard_container = page.locator("p.header-name")     ##Locates the dashboard title ,to check if dashboard has loaded
        self.avatar_initials = page.locator("img.MuiAvatar-img").first    ##Gets the first avatar,that shows your profile picture
        self.dropdown_arrow = page.locator("div.profile-click-icon-div img")   ##Locates the small dropdown arrow next to name to open menu
        self.logout_button = self.page.get_by_text("Log out")     ##Finds the logout text inside the menu dropdown
        ## .first is used because there were multiple matching elements

## Handles the "Download App" popup that blocks ui
    def close_popup_if_exists(self):
        ##locates the popup close button using accesible label
        popup_close = self.page.locator("button[aria-label='Close popup']")
        if popup_close.is_visible():   ##checks if popup is visible
            popup_close.click()      ##clicking upon it closes the popup
            self.page.wait_for_timeout(300)   ##waits 300ms to ensure ui updates

## Checks if dashboard page actually loaded
    def is_dashboard_loaded(self):
        ## starts a try block to avoid crashes if element isn't found
        try:
            expect(self.dashboard_container).to_be_visible()     ##Validates the dashboard title is visible
            return True       ## Returns success
        except:
            return False        ##if anything fails returns false instead of crashing

## main method to perform logout action
    def click_logout(self):
        ## Wraps logout steps in a try block
        try:
            self.close_popup_if_exists()     ##Closes the annoying popup if present
            expect(self.avatar_initials).to_be_visible()      ##Waits until avatar is visible(ensure page is loaded
            self.avatar_initials.click()                    ##Clicks profile image to open dropdown menu
            # expect(self.dropdown_arrow).to_be_visible()
            # self.dropdown_arrow.click()
            expect(self.logout_button).to_be_visible()      ##waits until logout item appears
            self.logout_button.click()                       ##Clicks the logout menu action
        except Exception as e:
            raise Exception("Logout button not clickable") from e
         ## If anything fails, throws a custom readable error

