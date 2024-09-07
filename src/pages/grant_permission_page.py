from src.pages.base_page import GenieBasePage

class GrantPage(GenieBasePage):
    def swipe_tem_from_right_to_left(self):
        window_size = self.driver.get_window_size()
        x = window_size["width"]
        y = window_size["height"]
        
        self.driver.swipe(start_x = x * 0.8,
                          start_y = y * 0.55,
                          end_x = x * 0.3,
                          end_y = y * 0.55,
                          duration = 1000)