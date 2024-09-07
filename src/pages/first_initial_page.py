from src.locators.first_initial_locators import FirstInitialLocators
from src.pages.base_page import IlabelerBasePage

class InitialPage(IlabelerBasePage):
    #swipe
    def swipe_from_right_to_left(self):
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        self.driver.swipe(start_x = x * 0.8,
                          start_y = y * 0.5,
                          end_x = x * 0.3,
                          end_y = y * 0.5,
                          duration = 1000)

    def swipe_from_left_to_right(self):
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        self.driver.swipe(start_x = x * 0.3,
                          start_y = y * 0.5,
                          end_x = x * 0.8,
                          end_y = y * 0.5,
                          duration = 1000)
