from src.locators.overview_locators import OverviewLocators
from src.pages.overview_page import OverViewPage


def new_a_label(driver):
    overview_page = OverViewPage(driver)
    overview_locator = OverviewLocators()
    try:
        if overview_page.element_visible(overview_locator.BUTTON_NEW, timeout=3):
            overview_page.click(overview_locator.BUTTON_NEW)
    except:
        overview_page.click(overview_locator.BUTTON_NEW_2)

    """
        if overview_page.new_button_visible(overview_locator.BUTTON_NEW, timeout=3):
        overview_page.click(overview_locator.BUTTON_NEW)
    else:
        overview_page.click(overview_locator.BUTTON_NEW_2)
    """

