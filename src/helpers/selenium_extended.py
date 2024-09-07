from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumExtended:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.default_timeout = 10

    def wait_and_locator(self, loc, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
    
    def wait_and_input_text(self, loc, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
             EC.visibility_of_element_located(loc)).send_keys(text)

    def wait_and_click(self, loc, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(loc)).click()

    def wait_and_element_contains_text(self, loc, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(loc, text))
        
    def wait_and_element_exist(self, loc, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        
        if WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(loc)):
            return True
        else:
            return False           
    
    def wait_and_text(self, loc, timeout=60):
        timeout = timeout if timeout else self.default_timeout
        text = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(loc)).text
        return text

    def wait_and_clear(self, loc, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(loc)).clear()

    def wait_and_element_new_button(self, loc, timeout=None):

        if not WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(loc)):
            return True
        else:
            return False         