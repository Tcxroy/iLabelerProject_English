from appium.webdriver.common.appiumby import AppiumBy
from src.helpers.device_screen import window_size_x, window_size_y

class EditLabelLocators:
    #select tape size
    TAPE_SIZE_1_INCHES = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="1 inches"]')
    TAPE_SIZE_3_4_INCHES = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="3/4 inches"]')
    TAPE_SIZE_1_2_INCHES = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="1/2 inches"]')
    TAPE_SIZE_3_8_INCHES = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="3/8 inches"]')
    TAPE_SIZE_1_4_INCHES = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="1/4 inches"]')
    HIDE_TAPE_SIZE_SELECTION = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup[6]/android.widget.ImageView')
    BUTTON_SET_TAPE_SIZE = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.view.ViewGroup/android.view.ViewGroup')
   
    #HEADER
    BUTTON_BACK = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView')
    
    BUTON_NEW = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.ImageView')
    BUTTON_SAVE = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.ImageView')
    BUTTON_PRINT = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.widget.ImageView')
    BUTTON_SETTING = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.widget.ImageView')
    #PREVIEW
    PREVIEW_LABEL = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup')
    PREVIEW_ZOOM = (
        AppiumBy.XPATH, '')
    
    # TEXTS INPUT
    
    INPUT_TEXT_1 = (
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    

    #SETTINGS
    SETTING_TAPE_SIZE_1_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="1"]')
    SETTING_TAPE_SIZE_3_4_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="3/4"]')
    SETTING_TAPE_SIZE_1_2_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="1/2"]')
    SETTING_TAPE_SIZE_3_8_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="3/8"]')
    SETTING_TAPE_SIZE_1_4_INCHES = (AppiumBy.XPATH, '//android.widget.TextView[@text="1/4"]')
    #SETTING_TAPE_SIZE_24_MM = (AppiumBy.XPATH, '')
    #SETTING_TAPE_SIZE_19_MM = (AppiumBy.XPATH, '')
    #SETTING_TAPE_SIZE_12_MM = (AppiumBy.XPATH, '')
    #SETTING_TAPE_SIZE_9_MM = (AppiumBy.XPATH, '')
    #SETTING_TAPE_SIZE_6_MM = (AppiumBy.XPATH, '')


    #TEXT FIELD
    ONE_LINE_TEXT = (AppiumBy.XPATH, '//android.widget.EditText')
    ADD_NEW_LINE = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView')
    
    FIRST_LINE_TEXT = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.EditText')
    SECOND_LINE_TEXT = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.EditText')
    
    # FONT STYLE
    #BUTTON_TEXT_STYLES = (AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup')
    #BUTTON_ICONS = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup')
    #BUTTON_BORDERS = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[4/android.view.ViewGroup/android.view.ViewGroup')
    #BUTTON_DATE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
    # SCROLL once , and xpath is same as date
    #BUTTON_BARCODE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
    # SCROLL twice , and xpath is same as date
    #BUTTON_SERIALIZE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
    # SCROLL 3 times , and xpath is same as date
    #BUTTON_HANDWRITING = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')
    # SCROLL 4 times , and xpath is same as date
    #BUTTON_BACKGROUND = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ImageView')


    #font
    FONT_audiowide = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Audiowide"])[2]')
    FONT_cairo = (AppiumBy.XPATH, '//android.widget.TextView[@text="Cairo"]')
    FONT_comfortaa = (AppiumBy.XPATH, '//android.widget.TextView[@text="Comfortaa"]')
    FONT_courgette = (AppiumBy.XPATH, '//android.widget.TextView[@text="Courgette"]')
    FONT_dancing_script = (AppiumBy.XPATH, '//android.widget.TextView[@text="Dancing Script"]')
    FONT_eczar = (AppiumBy.XPATH, '//android.widget.TextView[@text="Eczar"]')
    FONT_great_vibes = (AppiumBy.XPATH, '//android.widget.TextView[@text="Great Vibes"]')
    FONT_inconsolata = (AppiumBy.XPATH, '//android.widget.TextView[@text="Inconsolata"]')
    FONT_katibeh = (AppiumBy.XPATH, '//android.widget.TextView[@text="Katibeh"]')
    FONT_kaushan_script = (AppiumBy.XPATH, '//android.widget.TextView[@text="Kaushan Script"]')
    FONT_lobster = (AppiumBy.XPATH, '//android.widget.TextView[@text="Lobster"]')
    FONT_lora = (AppiumBy.XPATH, '//android.widget.TextView[@text="Lora"]')
    FONT_markazi_text = (AppiumBy.XPATH, '//android.widget.TextView[@text="Markazi Text"]')
    FONT_metal_mania = (AppiumBy.XPATH, '//android.widget.TextView[@text="Metal Mania"]')
    FONT_mystery_quest = (AppiumBy.XPATH, '//android.widget.TextView[@text="Mystery Quest"]')
    FONT_patrick_hand = (AppiumBy.XPATH, '//android.widget.TextView[@text="Patrick Hand"]')
    FONT_pirata_one = (AppiumBy.XPATH, '//android.widget.TextView[@text="Pirata One"]')
    FONT_playball = (AppiumBy.XPATH, '//android.widget.TextView[@text="Playball"]')
    FONT_poiret_one = (AppiumBy.XPATH, '//android.widget.TextView[@text="Poiret One"]')
    FONT_quicksand = (AppiumBy.XPATH, '//android.widget.TextView[@text="Quicksand"]')
    FONT_ribeye_marrow = (AppiumBy.XPATH, '//android.widget.TextView[@text="Ribeye Marrow"]')
    FONT_righteous = (AppiumBy.XPATH, '//android.widget.TextView[@text="Righteous"]')
    FONT_roboto_slab = (AppiumBy.XPATH, '//android.widget.TextView[@text="Roboto Slab"]')
    FONT_sacramento = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sacramento"]')
    FONT_sancreek = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sancreek"]')
    FONT_shadows_into_light_two = (AppiumBy.XPATH, '//android.widget.TextView[@text="Shadows Into Light Two"]')
    FONT_shojumaru = (AppiumBy.XPATH, '//android.widget.TextView[@text="Shojumaru"]')
    FONT_sourcecode_pro = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sourcecode Pro"]')

    BUTTON_FONT_APPLY = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
    BUTTON_FONT_CANCEL = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup')
    #FONT_ = (AppiumBy.XPATH, '')
    #font size 18-130

    #FONT_SIZE_18 =  (AppiumBy.XPATH, '//android.widget.TextView[@text="18"]')
    BUTTON_FONT_SIZE_APPLY = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup')
    BUTTON_FONT_SIZE_CANCEL = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup')
    
    #font styles
    FONT_BOLD = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup')
    FONT_ITALIC = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup')
    FONT_UNDERLINE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup')
    FONT_DELETE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.view.ViewGroup')
    FONT_OUTLINE = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup')
    FONT_SHADOW = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup')
    FONT_VERTICAL = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup')


    #FONT STYLES AREA
    BUTTON_FONT_STYLES = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="Text styles"]')
    BUTTON_ICONS = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="Icons"]')
    BUTTON_BORDERS= (
        AppiumBy.XPATH,'//android.widget.TextView[@text="Borders"]')
    BUTTON_DATE = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="Date"]')
    BUTTON_BARCODE = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="Barcode"]')
    BUTTON_SERIALIZE = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="Serialize"]')
    BUTTON_HANDWRITING = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="Handwriting"]')
    BUTTON_BACKGOUND = (
        AppiumBy.XPATH,'//android.widget.TextView[@text="Background"]')
    
    #FONT STYLES
    STYLE_FONTS = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup')
    STYLE_SIZES = (
        AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup')

    #icons
    GROUP_RECENT = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[1]')
    GROUP_2ND = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[2]')
    GROUP_3RD = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[3]')
    GROUP_4TH = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[4]')
    GROUP_5TH = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[5]')
    GROUP_6TH = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[6]')
    GROUP_7TH = (
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.HorizontalScrollView/android.view.ViewGroup/android.view.ViewGroup[7]')

    def locator_font_size(self, num=34):
        #size = (AppiumBy.XPATH, f'//android.widget.TextView[@text="{num}"]')
        font_size = str(num)
        size = (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{font_size}")')
        #print(size)
        return size

    def loctator_icon(self, row=1, col=1):
        if row>= 1 and row<= 4:
            if col>=1 and col<=6:
                icon= (AppiumBy.XPATH, f'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[{row}]/android.view.ViewGroup[{col}]/android.widget.ImageView')
            else:
                return None
        else:
                return None
        return icon
    
    #recent group can be one line, then the xpath will be changed. 
    '''
    def loctator_recent_icon_oneline(self, row=1):
        icon= (AppiumBy.XPATH, f'')
        return icon   
    
    
    '''

    #border
    def locator_border(self, num=1):
        if num >=1 and num < 15:
            border = (
                AppiumBy.XPATH, f'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[{num}]/android.view.ViewGroup/android.widget.ImageView')
        
        return border
    
    #Date and time
    BUTTON_CALENDER = (
         AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]')
    
    #NOT FINISHED
    BUTTON_CALENDER_OK = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')
    BUTTON_CALENDER_CANCEL = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="android:id/button2"]')
    CALENDER_CHOOSEN = (AppiumBy.ID, 'android:id/numberpicker_input')
    #CURR_YEAR = (AppiumBy.XPATH, '')
    #CURR_MONTH= (AppiumBy.XPATH, '')
    #CURR_DAY= (AppiumBy.XPATH, '')  

    #YEAR: f'//*[@bounds="[{x}*0.560,{y}*0.47][{x}*0.649,{y}*0.506]"]'
    #MONTH: f'//*[@bounds="[{x}*0.338,{y}*0.47][{x}*0.426,{y}*0.506]"]'
    #DAY: f'//*[@bounds="[{x}*0.449,{y}*0.47][{x}*0.537,{y}*0.506]"]'
    
    def locator_date(self, row=1, col=1):
        if col > 3 or col < 1:
            return None
        elif row >= 1 and row <= 8:
            date = (
                AppiumBy.XPATH, f'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[{col}]/android.view.ViewGroup[{row}]')
            return date
        
    