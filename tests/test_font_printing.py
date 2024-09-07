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
    data_for_bold_print = get_data_path("print_bold_all_sizes.csv")
    data_for_italic_print = get_data_path("print_italic_all_sizes.csv")
    data_for_outline_print = get_data_path("print_outline_all_sizes.csv")
    data_for_shadow_print = get_data_path("print_shadow_all_sizes.csv")
    data_for_vertical_print = get_data_path("print_vertical_all_sizes.csv")

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

    @allure.story('print bold style text')
    @pytest.mark.skipif(1==1,reason="not test")
    @pytest.mark.parametrize('case',read_csv(data_for_bold_print))
    def test_bold_style_print(self,android_driver,case):
        with allure.step('new a label'):
            new_a_label(android_driver)
        with allure.step('edit a bold style label'):
            edit_font(android_driver,case)
        with allure.step('print a label'):
            print_a_label(android_driver)
        with allure.step('get the print status'):
            result = printing_status(android_driver)
        with allure.step('Return back to home'):
            back_to_home(android_driver)
        assert result == 'Print successful'

    @allure.story('print italic style text')
    @pytest.mark.skip(reason="not test")
    @pytest.mark.parametrize('case',read_csv(data_for_italic_print))
    def test_italic_style_print(self,android_driver,case):
        with allure.step('new a label'):
            new_a_label(android_driver)
        with allure.step('edit a italic style label'):
            edit_font(android_driver,case)
        with allure.step('print a label'):
            print_a_label(android_driver)
        with allure.step('get the print status'):
            result = printing_status(android_driver)
        with allure.step('Return back to home'):
            back_to_home(android_driver)
        assert result == 'Print successful'
    
    @allure.story('print outline style text')
    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.parametrize('case',read_csv(data_for_outline_print))
    def test_outline_style_print(self,android_driver,case):
        with allure.step('new a label'):
            new_a_label(android_driver)
        with allure.step('edit a outline style label'):
            edit_font(android_driver,case)
        with allure.step('print a label'):
            print_a_label(android_driver)
        with allure.step('get the print status'):
            result = printing_status(android_driver)
        with allure.step('Return back to home'):
            back_to_home(android_driver)
        assert result == 'Print successful'
    
    @allure.story('print shadow style text')
    @pytest.mark.skip(reason="not test")
    @pytest.mark.parametrize('case',read_csv(data_for_shadow_print))
    def test_shadow_style_print(self,android_driver,case):
        with allure.step('new a label'):
            new_a_label(android_driver)
        with allure.step('edit a shadow style label'):
            edit_font(android_driver,case)
        with allure.step('print a label'):
            print_a_label(android_driver)
        with allure.step('get the print status'):
            result = printing_status(android_driver)
        with allure.step('Return back to home'):
            back_to_home(android_driver)
        assert result == 'Print successful'

    @allure.story('print vertical style text')
    @pytest.mark.skip(reason="not test")
    @pytest.mark.parametrize('case',read_csv(data_for_vertical_print))
    def test_vertical_style_print(self,android_driver,case):
        with allure.step('new a label'):
            new_a_label(android_driver)
        with allure.step('edit a vertical style label'):
            edit_font(android_driver,case)
        with allure.step('print a label'):
            print_a_label(android_driver)
        with allure.step('get the print status'):
            result = printing_status(android_driver)
        with allure.step('Return back to home'):
            back_to_home(android_driver)
        assert result == 'Print successful'


    #only can get the month
    @pytest.mark.skip(reason="not test")
    def test_add_date(self, android_driver):
        new_a_label(android_driver)
        add_a_date(android_driver, row=2, col=1)
        back_to_home(android_driver)
        #print_a_label(android_driver)
    @pytest.mark.skip(reason="not test")
    def test_add_border(self, android_driver):
        new_a_label(android_driver)
        add_a_border(android_driver, num=6)
        back_to_home(android_driver)
        #print_a_label(android_driver)
    @pytest.mark.skip(reason="not test")
    def test_select_date(self, android_driver):
        new_a_label(android_driver)
        add_a_date_from_calender(android_driver,day=5,month=3,year=2025)
        back_to_home(android_driver)
