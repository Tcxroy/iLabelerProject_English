#from src.locators.edit_label_locators import EditLabelLocators
from src.pages.edit_label_page import EditLabelPage
#from time import sleep
#from src.locators.print_locators import PrintLocators
from src.pages.print_page import PrintPage

def back_to_home(driver):
    edit_page = EditLabelPage(driver) 
    edit_page.click_button_back()

def back_to_edit(driver):
    edit_page = PrintPage(driver) 
    edit_page.select_button_back_to_editor()