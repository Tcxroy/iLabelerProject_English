from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy

class OverviewLocators:

    BUTTON_NEW  = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]')
    BUTTON_NEW_2 = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView')
    Text_OVERVIEW = (AppiumBy.XPATH, '//android.widget.TextView[@text="Overview"]')