import datetime
import pytest
from Library.excel import ReadExcel
from POMM.register_page import RegisterPage
from Library.config import Config


class TestRegisterPage:
    read_xl = ReadExcel()
    data = read_xl.read_data(Config.SHEET_NAME_DATA_PATH)

    @pytest.mark.parametrize("fname, lname, mail, pwd, cpwd", data)
    def test_valid_credentil(self, fname, lname, mail, pwd, cpwd, init_driver):
        driver = init_driver
        obj = RegisterPage(driver)
        try:

            obj = RegisterPage(init_driver)
            obj.click_register_link()
            obj.select_male_radio_btn()
            obj.enter_firstname(fname)
            obj.enter_lastname(lname)
            obj.enter_email(mail)
            actual_pwd = obj.enter_password(pwd)
            obj.confirm_password(cpwd, actual_pwd)

        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOT_PATH+name)
            raise error_msg
