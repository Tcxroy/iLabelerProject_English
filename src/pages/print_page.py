from src.locators.print_locators import PrintLocators
from appium.webdriver.common.touch_action import TouchAction
from src.pages.base_page import IlabelerBasePage

class PrintPage(IlabelerBasePage):
    def tap(self,el):
        loc = self.locator(el)
        actions = TouchAction(self.driver)
        actions.tap(loc)
        actions.perform()

    #Print settings pops up
    def select_print_button_on_print_setting(self):
        print_locator = PrintLocators()
        button = print_locator.BUTTON_PPRINT_ON_PRINT_SETTINGS
        return button
    
    def select_copies(self):
        print_locator = PrintLocators()
        input_button = print_locator.COPIES
        return input_button
    
    def select_mirror(self):
        print_locator = PrintLocators()
        toggle= print_locator.MIRROR_PRINT
        return toggle
    
    #multiprinters page     
    def get_text_select_printer(self):
        print_locator = PrintLocators()
        text_select_printer = print_locator.TEXT_SELECT_PRINTER
        return self.get_text(text_select_printer,timeout=5)

    def select_1st_printer(self):
        print_locator = PrintLocators()
        button = print_locator.SELECT_1ST_PRINTER # printer 1
        return button   
    
    def select_2nd_printer(self):
        print_locator = PrintLocators()
        button = print_locator.SELECT_2ND_PRINTER # printer 2
        return button  
    
    def select_specific_printer(self):
        print_locator = PrintLocators()
        button = print_locator.SELECT_PRINTER # F4:12:FA:8D:0B:FA
        return button  
         
    #Tape size mismatch page
    def get_text_tape_size_mismatch(self):
        print_locator = PrintLocators()
        text_mismatch = print_locator.TEXT_SIZE_MISMATCH
        return self.get_text(text_mismatch,timeout=5)
    
    def select_adjust_size_button(self):
        print_locator = PrintLocators()
        button = print_locator.BUTTON_ADJUST_LABEL_SIZE
        return button
    
    def select_print_button_on_mismatch(self):
        print_locator = PrintLocators()
        button = print_locator.BUTTON_PRINT_ON_MISMATCH
        return button
    
    def select_tape_size_1_inches(self):
        print_locator = PrintLocators()
        button = print_locator.TAPE_SIZE_1_INCHES
        return button

    def select_tape_size_3_4_inches(self):
        print_locator = PrintLocators()
        button = print_locator.TAPE_SIZE_3_4_INCHES
        return button
    
    def select_tape_size_1_2_inches(self):
        print_locator = PrintLocators()
        button = print_locator.TAPE_SIZE_1_2_INCHES
        return button
    
    def select_tape_size_3_8_inches(self):
        print_locator = PrintLocators()
        button = print_locator.TAPE_SIZE_3_8_INCHES
        return button
    
    def select_tape_size_1_4_inches(self):
        print_locator = PrintLocators()
        button = print_locator.TAPE_SIZE_1_4_INCHES
        return button
    
    def select_print_button_on_tape_size(self):
        print_locator = PrintLocators()
        button = print_locator.BUTTON_PRINT_ON_TAPE_SIZE
        return button
    
    def select_button_back_to_editor(self):
        print_locator = PrintLocators()
        button = print_locator.BUTTON_BACK_TO_EDITOR
        return button      
    
    def select_back(self):
        print_locator = PrintLocators()
        button = print_locator.BUTTON_BACK
        return button       
    
    #printer error
    def select_button_retry(self):
        print_locator = PrintLocators()
        button = print_locator.BUTTON_RETRY
        return button    
    
    def get_text_print_error(self):
        print_locator = PrintLocators()
        text_error = print_locator.TEXT_PRINTING_ERROR
        return self.get_text(text_error)        
    
    def get_text_pairing_failed(self):
        print_locator = PrintLocators()
        text_failed = print_locator.TEXT_PAIRING_FAILED
        return self.get_text(text_failed,timeout=5)  

    def get_text_print_successful(self):
        print_locator = PrintLocators()
        text_successful = print_locator.TEXT_PRINTING_SUCCESSFUL
        return self.get_text(text_successful,timeout=60)  
