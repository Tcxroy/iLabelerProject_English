#from src.locators.edit_label_locators import EditLabelLocators
from src.pages.edit_label_page import EditLabelPage
from src.pages.print_page import PrintPage
from time import sleep

def print_pairing_failed(driver):
    print_page = PrintPage(driver)
    try:
        text_failed = print_page.get_text_pairing_failed()
        if text_failed == 'Pairing failed':
            button = print_page.select_button_back_to_editor
            print_page.click(button)
    except:
        pass

def printer_selecter(driver):
    print_page = PrintPage(driver) 
    print("enter printer select page")
    try:
        text_printer_selecter = print_page.get_text_select_printer()
        if text_printer_selecter == "Select a printer":
            #text = print_page.get_text_select_printer
            printer = print_page.select_specific_printer()
            #printer = print_page.select_1st_printer()
            print_page.click(printer)
    except:
        #print_pairing_failed(driver)
        pass

def tape_size_mismatch(driver):
    print_page = PrintPage(driver)
    try:
        text_mismatch = print_page.get_text_tape_size_mismatch()
        #print(text_mismatch)
        if text_mismatch == 'Tape size mismatch':
            button = print_page.select_adjust_size_button()
            print_page.click(button)
            button = print_page.select_print_button_on_tape_size()
            print_page.click(button)
    except:
        #print("Tape size is matched")
        pass

def print_a_label(driver):
    edit_page = EditLabelPage(driver)
    #print_button_1 = EditLabelLocators.BUTTON_PRINT
    #edit_page.click(print_button_1)
    edit_page.click_button_print()
    print_page = PrintPage(driver)
    print_button_2 = print_page.select_print_button_on_print_setting()
    print_page.click(print_button_2)
    printer_selecter(driver)
    tape_size_mismatch(driver)    


def printing_status(driver):
    printing_page = PrintPage(driver)
    print_success = printing_page.get_text_print_successful()
    print(print_success)
    sleep(5)
    return print_success
    