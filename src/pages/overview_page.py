from src.locators.overview_locators import OverviewLocators
from src.pages.base_page import IlabelerBasePage


class OverViewPage(IlabelerBasePage):

    def swipe_temp_from_right_to_left(self):
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        element = IlabelerBasePage.element_visible(self, loc=OverviewLocators.BUTTON_AD_COLLASPE)
        if element:
            self.driver.swipe(start_x = x * 0.8,
                start_y = y * 0.55,
                end_x = x * 0.3,
                end_y = y * 0.55,
                duration = 1000)
        else:
            self.driver.swipe(start_x = x * 0.8,
                start_y = y * 0.25,
                end_x = x * 0.3,
                end_y = y * 0.25,
                duration = 1000)           

    def swipe_temp_from_left_to_right(self):
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        element = IlabelerBasePage.element_visible(self, loc=OverviewLocators.BUTTON_AD_COLLASPE)
        if element:
            self.driver.swipe(start_x = x * 0.3,
                start_y = y * 0.55,
                end_x = x * 0.8,
                end_y = y * 0.55,
                duration = 1000)
        else:
            self.driver.swipe(start_x = x * 0.3,
                start_y = y * 0.25,
                end_x = x * 0.8,
                end_y = y * 0.25,
                duration = 1000)   