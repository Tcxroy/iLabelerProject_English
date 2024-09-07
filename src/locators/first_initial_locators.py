from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

class FirstInitialLocators:
    BUTTON_SKIP = (AppiumBy.XPATH, '')
    
    BUTTON_NEXT = (
        AppiumBy.XPATH, '')

    BUTTON_START = BUTTON_NEXT
    
    BUTTON_DISGREE = (AppiumBy.XPATH, '')
    BUTTON_GREE = (AppiumBy.XPATH, '')

    LINK_PRIVACE = (AppiumBy.XPATH, '')
    LINK_USER_AGREEMENT = (AppiumBy.ANDROID_UIAUTOMATOR, '')
    
 