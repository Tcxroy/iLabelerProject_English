from appium.webdriver.common.appiumby import AppiumBy

class PrintLocators:
    TEXT_BLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("No Bluetooth")')

    BUTTON_PERMISSION_ALLOW = (AppiumBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    BUTTON_PERMISSION_DENY= (AppiumBy.ID, "com.android.packageinstaller:id/permission_deny_button")

    BUTTON_ALLOW_ONLY = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')

    TEXT_PRINT_NO_BLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("No Bluetooth")')
    BUTTON_BLE_TURN_ON = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup')
    BUTTON_BACK_TO_EDITOR = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup')

    TEXT_PRINT_SUCCESSFUL = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Print successful")')
    TEXT_PRINT_NOT_FOUND = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Print not found")')
    #BUTTON_RETRY = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup')

    TEXT_PRINT_NO_LOCATION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Location is off")')
    BUTTON_TURN_ON_LOCATION = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[1]/android.view.ViewGroup')
    BUTTON_OK_TURN_ON_LOC = (AppiumBy.ID, 'android:id/button1')
    BUTTON_NO_TURN_ON_LOC = (AppiumBy.ID, 'android:id/button2')

    #BUTTON_RETRY = BUTTON_TURN_ON_LOCATION  #SAME XPATH


    BUTTON_PPRINT_ON_PRINT_SETTINGS = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Print"])[2]')
    COPIES = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup')
    MIRROR_PRINT = (AppiumBy.XPATH, '//android.widget.Switch')

    BUTTON_BACK = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
    TEXT_SELECT_PRINTER = (AppiumBy.XPATH, '//android.widget.TextView[@text="Select a printer"]')

    #CAN REPLACE THE MAC ADDRESS 
    SELECT_PRINTER = (AppiumBy.XPATH, '//android.widget.TextView[@text="F4:12:FA:8D:0B:FA"]')

    SELECT_1ST_PRINTER = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]')
    SELECT_2ND_PRINTER = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]')
    #SELECT_3RD_PRINTER = (AppiumBy.XPATH, '')

    TEXT_SIZE_MISMATCH = (AppiumBy.XPATH, '//android.widget.TextView[@text="Tape size mismatch"]')
    BUTTON_PRINT_ON_MISMATCH = (AppiumBy.XPATH, '//android.widget.TextView[@text="Print"]')
    BUTTON_ADJUST_LABEL_SIZE= (AppiumBy.XPATH, '//android.widget.TextView[@text="Adjust label size"]')
    TAPE_SIZE_1_INCHES= (AppiumBy.XPATH, '//android.widget.TextView[@text="1 inches"]')
    TAPE_SIZE_3_4_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="3/4 inches"]')
    TAPE_SIZE_1_2_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="1/2 inches"]')
    TAPE_SIZE_3_8_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="3/8 inches"]')
    TAPE_SIZE_1_4_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="1/4 inches"]')

    BUTTON_PRINT_ON_TAPE_SIZE = (AppiumBy.XPATH,'(//android.widget.TextView[@text="Print"])[2]')
    BUTTON_CLOSE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ImageView')

    # PRINT
    
    BUTTON_BACK_TO_EDITOR = (AppiumBy.XPATH,'//android.widget.TextView[@text="Back to label editor"]')

    # PRINT ERROR
    TEXT_PRINTING_ERROR= (AppiumBy.XPATH, '//android.widget.TextView[@text="Printing error"]')
    # PRINT COMPLETE
    TEXT_PRINTING_COMPLETE= (AppiumBy.XPATH, '//android.widget.TextView[@text="Printing complete"]')
    TEXT_PRINTING_SUCCESSFUL= (AppiumBy.XPATH, '//android.widget.TextView[@text="Print successful"]')

    #PAIRING FAILED

    TEXT_PAIRING_FAILED = (AppiumBy.XPATH, '//android.widget.TextView[@text="Pairing failed"]')
    BUTTON_RETRY = (AppiumBy.XPATH, '//android.widget.TextView[@text="Retry"]')

    TEXT_SEARCHING = (AppiumBy.XPATH, '//android.widget.TextView[@text="Searching..."]')

    TEXT_CONNECTING = (AppiumBy.XPATH, '//android.widget.TextView[@text="Connecting"]')

    TEXT_SENDING_DATA = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sending data"]')
    
    TEXT_CUTTING = (AppiumBy.XPATH, '//android.widget.TextView[@text="Cutting"]')
    
    TEXT_PRINTING = (AppiumBy.XPATH, '//android.widget.TextView[@text="Printing"]')