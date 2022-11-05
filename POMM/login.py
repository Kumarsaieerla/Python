import re
from Library.excel import ReadExcel


class Login:
    read_xl = ReadExcel()
    registr_locater = read_xl.read_data()