from src.util.read_csv_file import read_csv
import pytest
from src.helpers.create_label import new_a_label
from src.helpers.edit_label import edit_font, add_an_icon, add_a_border, add_a_date, add_a_date_from_calender
from src.helpers.print_label import print_a_label
from src.helpers.print_label import printing_status
from src.helpers.return_to_home import back_to_home
from src.helpers.data_path import get_data_path
import allure

@allure.feature("Print testing")
@pytest.mark.usefixtures("appium_service")
class TestFontPrint:
    data_for_normal_print = get_data_path("print_normal_all_sizes.csv")

    @allure.story('print normal style text')
    #@pytest.mark.skip(reason="not test")
    #@pytest.mark.timeout(300)
    @pytest.mark.parametrize('case',read_csv(data_for_normal_print))
    #@pytest.mark.parametrize('case',read_csv(r"src\data\\print_normal_all_sizes.csv"))
    def test_normal_style_print(self,android_driver,case):
        with allure.step('new a label'):
            new_a_label(android_driver)
        with allure.step('edit a normal style label'):
            edit_font(android_driver,case)
        with allure.step('print a label'):
            print_a_label(android_driver)
        with allure.step('get the print status'):
            result = printing_status(android_driver)
        with allure.step('Return back to home'):
            back_to_home(android_driver)
        assert result == 'Print successful'

