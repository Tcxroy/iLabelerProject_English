from src.pages.base_page import IlabelerBasePage
from src.locators.edit_label_locators import EditLabelLocators
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.extensions.action_helpers import ActionHelpers
from src.helpers.device_screen import window_size_x, window_size_y
from src.helpers.current_date import current_date

class EditLabelPage(IlabelerBasePage):
    def click_button_back(self):
        edit_locator = EditLabelLocators()
        try:
            if self.element_visible(edit_locator.BUTTON_BACK):
                self.click(edit_locator.BUTTON_BACK)
        except:
            raise("The screen not go back to edit view")

    def click_button_new(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTON_NEW)

    def click_button_save(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_SAVE)

    def click_button_print(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_PRINT)

    def click_button_settings(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_SETTING)

    def click_add_extra_line(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.ADD_NEW_LINE)

    def tap(self,el):
        loc = self.locator(el)
        actions = TouchAction(self.driver)
        actions.tap(loc)
        actions.perform()

    def zoom_in(self):
        x = window_size_x(self.driver)
        y = window_size_y(self.driver)
        #preview_label = EditLabelLocators.PREVIEW_LABEL
        a1 = TouchAction()
        a1.press(x=x*0.7, y=y*0.3)
        a1.wait(500)
        a1.move_to(x=x*0.5, y=y*0.35)
        a1.release()

        a2 = TouchAction()
        a2.press(x=x*0.25, y=y*0.4)
        a2.wait(500)
        a2.move_to(x=x*0.35, y=y*0.35)
        a2.release()

        ma = MultiAction(self.driver)
        ma.add(a1, a2)
        ma.perform()

    def zoom_out(self):
        x = window_size_x(self.driver)
        y = window_size_y(self.driver)
        #preview_label = EditLabelLocators.PREVIEW_LABEL
        a1 = TouchAction()
        a1.press(x=x*0.55, y=y*0.35)
        a1.wait(500)
        a1.move_to(x=x*0.7, y=y*0.3)
        a1.release()

        a2 = TouchAction()
        a2.press(x=x*0.45, y=y*0.35)
        a2.wait(500)
        a2.move_to(x=x*0.25, y=y*0.4)
        a2.release()

        ma = MultiAction(self.driver)
        ma.add(a1, a2)
        ma.perform()

    #swipe icon, date list
    def swipe_down(self):
        x = window_size_x(self.driver)
        y = window_size_y(self.driver)
        self.driver.swipe(start_x = x * 0.8,
                          start_y = y * 0.8,
                          end_x = x * 0.8,
                          end_y = y * 0.75,
                          duration = 1000)
    def swipe_up(self):
        x = window_size_x(self.driver)
        y = window_size_y(self.driver)
        self.driver.swipe(start_x = x * 0.8,
                          start_y = y * 0.75,
                          end_x = x * 0.8,
                          end_y = y * 0.8,
                          duration = 1000)
    # swipe font    
    def swipe_font_down(self):
        x = window_size_x(self.driver)
        y = window_size_y(self.driver)
        self.driver.swipe(start_x = x * 0.8,
                          start_y = y * 0.8,
                          end_x = x * 0.8,
                          end_y = y * 0.4,
                          duration = 1000)
    def swipe_font_up(self):
        x = window_size_x(self.driver)
        y = window_size_y(self.driver)
        self.driver.swipe(start_x = x * 0.8,
                          start_y = y * 0.4,
                          end_x = x * 0.8,
                          end_y = y * 0.8,
                          duration = 1000)
    # swipe font size  
    def swipe_font_size_down(self):
        x = window_size_x(self.driver)
        y = window_size_y(self.driver)
        self.driver.swipe(start_x = x * 0.8,
                          start_y = y * 0.8,
                          end_x = x * 0.8,
                          end_y = y * 0.4,
                          duration = 1000)
    def swipe_font_size_up(self):
        x = window_size_x(self.driver)
        y = window_size_y(self.driver)
        self.driver.swipe(start_x = x * 0.8,
                          start_y = y * 0.4,
                          end_x = x * 0.8,
                          end_y = y * 0.8,
                          duration = 1000)

    def click_button_text_styles(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_FONT_STYLES)

    def click_button_icons(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_ICONS) 

    def click_button_borders(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_BORDERS) 

    def click_button_date(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_DATE) 

    def click_button_bacode(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_BARCODE) 

    def click_button_serialize(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_SERIALIZE) 

    def click_button_handwriting(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_HANDWRITING)

    def click_button_background(self):
        edit_locator = EditLabelLocators()
        self.click(edit_locator.BUTTON_BACKGOUND) 

    def select_font(self, font_name):
        edit_locator = EditLabelLocators()
        name = str.lower(font_name)
        name = name.replace(" ", "_")
        font = "FONT_" + name
        #动态调用font
        #element_font = getattr(edit_locator, font)
        #from current to end
        while True:
            try:
                if self.element_visible(getattr(edit_locator, font), timeout=1):
                    self.click(getattr(edit_locator, font))
                    break
            except:
                #self.swipe_down()
                self.swipe_font_down()
                try:
                    if self.element_visible(edit_locator.FONT_sourcecode_pro, timeout=1):
                        if self.element_visible(getattr(edit_locator, font), timeout=1):
                            print(3)
                            self.click(getattr(edit_locator, font))
                            break
                        break
                except:
                        continue
        #from end to start
        while True:
            try:
                if self.element_visible(getattr(edit_locator, font), timeout=1):
                    self.click(getattr(edit_locator, font))
                    break
            except:
                #self.swipe_up()
                self.swipe_font_up()
                try:
                    if self.element_visible(edit_locator.FONT_audiowide, timeout=1):
                        if self.element_visible(getattr(edit_locator, font), timeout=1):
                            self.click(getattr(edit_locator, font))
                            break
                        break
                except:
                        continue

    def select_style(self, font_style, font_name):
        if font_style == '':
            pass
        elif  font_style == 'bold': 
            self.click(EditLabelLocators.FONT_BOLD)  
        elif font_style == 'italic':   
            self.click(EditLabelLocators.FONT_ITALIC)
        elif font_style == 'underline':
            self.click(EditLabelLocators.FONT_UNDERLINE)
        elif font_style == 'outline':  
            self.click(EditLabelLocators.FONT_OUTLINE)   
        elif font_style == 'shadow':   
            self.click(EditLabelLocators.FONT_SHADOW)
        elif font_style == 'delete':   
            self.click(EditLabelLocators.FONT_DELETE)
        elif font_style == 'vertical': 
            if font_name == 'vintage':
                self.click(EditLabelLocators.STYLE_VINTAGE_VERTICAL)
            else:
                self.click(EditLabelLocators.FONT_VERTICAL)
#in use
    def select_font_size(self, font_size):
        font_size = int(font_size)
        if font_size == '':
            pass
        elif font_size < 8 or font_size > 130:
            pass
        else:
            min_font_size = 8
            max_font_size = 130
            if font_size < 34:
                while True:
                    try:
                        edit_locator = EditLabelLocators()
                        locator = edit_locator.locator_font_size(num=font_size)
                        if self.element_visible(locator, timeout=1):
                            self.click(locator)
                            break
                    except:
                        self.swipe_font_size_up()
                        try:
                            min_locator = edit_locator.locator_font_size(num=min_font_size)
                            if self.element_visible(min_locator, timeout=1):
                                if self.element_visible(locator, timeout=1):
                                    self.click(locator)
                                    break
                                break
                        except:
                            continue          
            else:
                while True:
                    try:
                        edit_locator = EditLabelLocators()
                        locator = edit_locator.locator_font_size(num=font_size)
                        if self.element_visible(locator, timeout=1):
                            self.click(locator)
                            break
                    except:
                        self.swipe_font_size_down()
                        try:
                            max_locator = edit_locator.locator_font_size(num=max_font_size)
                            if self.element_visible(max_locator, timeout=1):
                                if self.element_visible(locator, timeout=1):
                                    self.click(locator)
                                    break
                                break
                        except:
                            continue                 

    #not use
    def new_font_szie(self, font_size):
        font_size = int(font_size)
        if font_size == '':
            pass
        elif font_size < 8 or font_size > 130:
            pass
        else:
            min_font_size = 8
            max_font_size = 130
            while True:
                try:
                    edit_locator = EditLabelLocators()
                    locator = edit_locator.locator_font_size(num=font_size)
                    if self.element_visible(locator, timeout=1):
                        self.click(locator)
                        break
                except:
                    self.swipe_font_size_down()
                    try:
                        max_locator = edit_locator.locator_font_size(num=max_font_size)
                        if self.element_visible(max_locator, timeout=1):
                            if self.element_visible(locator, timeout=1):
                                self.click(locator)
                                break
                            break
                    except:
                        continue      

            while True:
                try:
                    edit_locator = EditLabelLocators()
                    locator = edit_locator.locator_font_size(num=font_size)
                    if self.element_visible(locator, timeout=1):
                        self.click(locator)
                        break
                except:
                    self.swipe_font_size_up()
                    try:
                        min_locator = edit_locator.locator_font_size(num=min_font_size)
                        if self.element_visible(min_locator, timeout=1):
                            if self.element_visible(locator, timeout=1):
                                self.click(locator)
                                break
                            break
                    except:
                        continue          
                            
    #not use
    def select_icon(self, row, col):
        try:
            edit_locator = EditLabelLocators()
            icon = edit_locator.loctator_icon(row, col)
        except:
            raise('The row of icon should be between 1 and 4, col should be between 1 and 6')
        self.click(icon)
     #not use
    def select_border(self, num):
        try:
            edit_locator = EditLabelLocators()
            border = edit_locator.locator_border(num=num)
        except:
            raise('The number should be between 1 and 15')
        self.click(border)

    def select_date_from_calender(self, driver, day, month, year):
        curr_day, curr_month, curr_year = current_date(driver)
        #print(curr_day)
        #print(curr_month)
        #print(curr_year)
        #month_dict={'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6,'Jul':7,'Aug':8, 'Sep':9,'Oct':10, 'Nov':11, 'Dec':12}
        #month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        while True:
            x = window_size_x(self.driver)
            y = window_size_y(self.driver)
            if year == curr_year and month == curr_month and day == curr_day:
                break

            # 移动day，[485,901][581,973]
            if day > int(curr_day):
                self.driver.swipe(start_x=x*0.45, 
                                  start_y=y*0.47, 
                                  end_x=x*0.45, 
                                  end_y=y*0.39, 
                                  duration=1000)
                day -= 1 
            elif day< int(curr_day):
                self.driver.swipe(start_x=x*0.45, 
                                  start_y=y*0.47, 
                                  end_x=x*0.45, 
                                  end_y=y*0.55, 
                                  duration=1000)
                day += 1
            # 移动月份，[365,901][461,973]
            if month > int(curr_month):
                self.driver.swipe(start_x=x*0.338, 
                                  start_y=y*0.47, 
                                  end_x=x*0.338, 
                                  end_y=y*0.39, 
                                  duration=1000)
                month -= 1
            elif month < int(curr_month):
                self.driver.swipe(start_x=x*0.338, 
                                  start_y=y*0.47, 
                                  end_x=x*0.338, 
                                  end_y=y*0.55, 
                                  duration=1000)
                month += 1
            # 移动年份，[605,901][701,973]
            if year > int(curr_year):
                self.driver.swipe(start_x=x*0.57, 
                                  start_y=y*0.47, 
                                  end_x=x*0.52, 
                                  end_y=y*0.39, 
                                  duration=1000)
                year -= 1
            elif year < int(curr_year):
                self.driver.swipe(start_x=x*0.57, 
                                  start_y=y*0.47, 
                                  end_x=x*0.52, 
                                  end_y=y*0.55, 
                                  duration=1000)
                year += 1
                
    def select_date(self, row, col):
        #try:
        edit_locator = EditLabelLocators()
        self.click(edit_locator.locator_date(int(row), int(col)))
        #except:
            #raise('The row should be between 1 and 8')


    def select_tape_size_in_label_settings(self,tape_size=1):
        edit_locator = EditLabelLocators()
        if tape_size == '1' or tape_size == '24':
            self.click(edit_locator.SETTING_TAPE_SIZE_1_INCHES)
        elif tape_size == '3/4' or tape_size == '19':
            self.click(edit_locator.SETTING_TAPE_SIZE_3_4_INCHES)
        elif tape_size == '1/2' or tape_size == '12':
            self.click(edit_locator.SETTING_TAPE_SIZE_1_2_INCHES)
        elif tape_size == '3/8' or tape_size == '9':
            self.click(edit_locator.SETTING_TAPE_SIZE_3_8_INCHES)
        elif tape_size == '1/4' or tape_size == '6':
            self.click(edit_locator.SETTING_TAPE_SIZE_1_4_INCHES)