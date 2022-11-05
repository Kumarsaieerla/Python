import re
from Library.excel import ReadExcel
from Library.config import Config

class RegisterPage:

    read_xl = ReadExcel()
    reg_locators = read_xl.read_locaters(Config.SHEET_NAME_LOCATER_PATH)

    def __init__(self, driver):
        self.driver = driver

    def click_register_link(self):
        locator = self.reg_locators["click_register_link"]
        self.driver.find_element(*locator).click()

    def select_male_radio_btn(self):
        locator = self.reg_locators["select_male_radio_btn"]
        self.driver.find_element(*locator).click()

    def enter_firstname(self,fname):
        locator = self.reg_locators["enter_firstname"]
        self.driver.find_element(*locator).send_keys(fname)

    def enter_lastname(self, lname):
        locator = self.reg_locators["enter_lastname"]
        self.driver.find_element(*locator).send_keys(lname)
    def enter_email(self, mail):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, mail)
        assert result, "invalid email"

        locator = self.reg_locators["enter_email"]
        self.driver.find_element(*locator).send_keys(mail)

    def enter_password(self, pwd):
        assert len(pwd) >= 6, "password should have atleast 6 characters"

        locator = self.reg_locators["enter_password"]
        self.driver.find_element(*locator).send_keys(pwd)
        return pwd

    def confirm_password(self, cpwd, actual_pwd):
        locator = self.reg_locators["confirm_password"]
        assert actual_pwd == cpwd, "passwords are different"
        self.driver.find_element(*locator).send_keys(cpwd)
        self.driver.find_element(*locator).send_keys(cpwd)
