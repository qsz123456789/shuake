import logging
import unittest
from time import sleep
from parameterized import parameterized
from selenium import webdriver

from base import log
from base.base import Base
from page.page_course import PageCourse
from page.page_login import PageLogin
from page.page_personal_space import PagePersonalSpace
from page.page_learning import PageLearning
from util import GetDriver, read_json



class TestLogin(unittest.TestCase):
    def setUp(self)->None:
        self.driver=GetDriver.get_web_driver()
        #获取实例
        self.base=Base(self.driver)
        self.login=PageLogin(self.driver)
        self.personnal_space=PagePersonalSpace(self.driver)
        self.course=PageCourse(self.driver)
        self.learning=PageLearning(self.driver)
    def tearDown(self)->None:
        sleep(5)
        self.driver.quit()
    @parameterized.expand(read_json("course.json","course"))
    def test01_login(self,phone,pwd,value):
        try:
            self.login.page_login(phone,pwd)
            #获取昵称
            nickname=self.login.page_get_nickname()
            print("昵称为：", nickname)
            self.personnal_space.page_personal_space(value)
            #for i in range(100):
            self.course.page_course()
            self.learning.page_learning()
        except Exception as e:
            log.error(e)
            #截图
            self.base.base_get_img()
            #抛异常
            raise


