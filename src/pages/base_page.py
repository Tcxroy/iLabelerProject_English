from src.helpers.selenium_extended import SeleniumExtended
from appium import webdriver
class IlabelerBasePage:
    default_timeout = 3

    def __init__(self,driver) -> None:
        self.driver = driver
        self.se_driver = SeleniumExtended(self.driver)

    def get_text(self, loc,timeout):
        return self.se_driver.wait_and_text(loc, timeout)

    def input(self, loc, value):
        #loc is a turple
        self.se_driver.wait_and_input_text(loc, value)

    def click(self, loc):
        #loc is a turple
        self.se_driver.wait_and_click(loc)

    def element_contains_text(self, loc, value):
        #loc is a turple
        self.se_driver.wait_and_element_contains_text(loc,value)

    def element_visible(self, loc,timeout=None):
        timeout = timeout if timeout else self.default_timeout
        elem_exist = self.se_driver.wait_and_element_exist(loc,timeout)
        return elem_exist

    def locator(self,loc):
        return self.se_driver.wait_and_locator(loc)
    
    def clear(self,loc):
        self.se_driver.wait_and_clear(loc)

    def new_button_visible(self, loc, timeout=None):
        elem_exist = self.se_driver.wait_and_element_new_button(loc,timeout)
        return elem_exist
