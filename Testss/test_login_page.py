import pytest
from POMM.login import LoginPage
from Library.excel import ReadExcel
from config import config

class TestLoginPage:
    read_xl = ReadExcel()
    data = read_xl.read_testdata()

    @pytest.mark.parametrize("email, pwd",data)
    def test_login(self,init_driver,email,pwd):

        driver = init_driver
        lp = LoginPage(driver)
        lp.click_login_link()
        lp.enetr_email(email)
        lp.enetr_password()
