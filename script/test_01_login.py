import unittest
from selenium import webdriver
from page.page_login import PageLogin


class TestLogin(unittest.TestCase):
    def setUp(self)->None:
        self.driver=webdriver.Chrome(r"E:\chrome-win64\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://passport2.chaoxing.com/login?fid=12&refer=http%3A%2F%2Fi.chaoxing.com%2Fbase%3Ft%3D1700024040825&space=2")

        self.login=PageLogin(self.driver)

    def tearDown(self)->None:
        self.driver.quit()
    def test01_login(self,phone="17713483937",pwd="*z$913129"):
        self.login.page_login(phone,pwd)
        nickname=self.login.page_get_nickname()
        print("昵称为：", nickname)


