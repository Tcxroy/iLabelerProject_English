from src.locators.edit_label_locators import EditLabelLocators
from src.pages.edit_label_page import EditLabelPage

def tape_size_chosen(driver):
    tape_size_selection = EditLabelPage(driver)
    #default selection and confim with the button 'set tape size'
    tape_size_selection.click(EditLabelLocators.BUTTON_SET_TAPE_SIZE) 