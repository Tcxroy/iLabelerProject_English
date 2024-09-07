from src.locators.overview_locators import OverviewLocators
from src.pages.overview_page import OverViewPage
from src.locators.edit_label_locators import EditLabelLocators
from src.pages.edit_label_page import EditLabelPage

class Step():

    def new_a_label(self, driver):
        overview_page = OverViewPage(driver)
        overview_locator = OverviewLocators()
        try:
            if overview_page.element_visible(overview_locator.BUTTON_NEW, timeout=3):
                overview_page.click(overview_locator.BUTTON_NEW)
        except:
            overview_page.click(overview_locator.BUTTON_NEW_2)

    def save_a_label(self, driver):
        edit_page = EditLabelPage(driver) 
        #edit_page.click(EditLabelLocators.BUTTON_SAVE)
        edit_page.click_button_save()

    def click_date(self, driver):
        pass

    def edit_font(self, driver, data):
        edit_page = EditLabelPage(driver)
        edit_locator = EditLabelLocators()
        edit_page.clear(EditLabelLocators.INPUT_TEXT_1)
        edit_page.input(EditLabelLocators.INPUT_TEXT_1, data['input_text'])
        edit_page.click(EditLabelLocators.BUTTON_FONT_STYLES)  
        edit_page.click(EditLabelLocators.STYLE_FONTS) 
        edit_page.select_font(data['fonts'])
        edit_page.click(EditLabelLocators.BUTTON_FONT_APPLY)
        
        edit_page.select_style(data['styles'], data['fonts'])
        
        edit_page.click(EditLabelLocators.STYLE_SIZES) 
        edit_page.select_font_size(data['sizes'])
        #edit_page.new_font_szie(data['sizes'])
        #select_size = edit_locator.locator_font_size(num=data['sizes'])
        #edit_page.click(select_size)
        edit_page.click(EditLabelLocators.BUTTON_FONT_SIZE_APPLY)

        self.save_a_label(driver)


    def add_an_icon(self, driver, row, col):
        edit_page = EditLabelPage(driver) 
        edit_locator = EditLabelLocators()
        edit_page.click(edit_locator.BUTTON_ICONS)
        icon = edit_locator.loctator_icon(row, col)
        edit_page.click(icon)
        edit_page.click(edit_locator .BUTTON_SAVE)

    def add_a_border(self, driver, case):
        edit_page = EditLabelPage(driver)
        edit_locator = EditLabelLocators()
        edit_page.click(edit_locator.BUTTON_BORDERS)
        num = case['index']
        border = edit_locator.locator_border(num=int(num))
        edit_page.click(border)
        edit_page.click(edit_locator.BUTTON_SAVE) 

    def add_a_date(self, driver, row, col):
        edit_page = EditLabelPage(driver)
        edit_locator = EditLabelLocators()
        edit_page.click(edit_locator.BUTTON_DATE)
        date = edit_locator.locator_date(row, col)
        edit_page.click(date)
        #edit_page.select_date(row=int(row), col=int(col))
        edit_page.click(EditLabelLocators.BUTTON_SAVE)  

    def add_a_date_from_calender(self,driver, day, month, year, row = 1, col = 1):
        edit_page = EditLabelPage(driver)
        edit_locator = EditLabelLocators()

        edit_page.click(edit_locator.BUTTON_DATE)
        edit_page.click(edit_locator.BUTTON_CALENDER)
        edit_page.select_date_from_calender(driver, day, month, year)
        edit_page.click(edit_locator.BUTTON_CALENDER_OK)

        edit_page.click(EditLabelLocators.BUTTON_SAVE) 
        date = edit_locator.locator_date(row, col)
        edit_page.click(date)

        self.save_a_label(driver)