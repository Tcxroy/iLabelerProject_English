def window_size_x(driver):
    size = driver.get_window_size()
    x = size["width"]
    return x

def window_size_y(driver):
    size = driver.get_window_size()
    y = size["height"]
    return y