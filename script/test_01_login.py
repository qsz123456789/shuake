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
from util import DriverUtil, read_json



class TestLogin(unittest.TestCase):
    def setUp(self)->None:
        self.driver=DriverUtil.get_web_driver()
        #获取实例
        self.base=Base(self.driver)
        self.login=PageLogin(self.driver)
        self.personnal_space=PagePersonalSpace(self.driver)
        self.course=PageCourse(self.driver)
        self.learning=PageLearning(self.driver)
    def tearDown(self)->None:
        #DriverUtil.quit_web_driver()
        sleep(1)
        self.driver.quit()
    @parameterized.expand(read_json("course.json","course"))
    def test01_login(self,phone,pwd,value):
        try:
            self.login.page_login(phone,pwd)
            #获取昵称
            nickname=self.login.page_get_nickname()
            print("昵称为：", nickname)
            self.personnal_space.page_personal_space(value)
            self.course.page_course()
            for i in range(100):
                self.driver.switch_to.frame(0)
                not_sees = self.driver.find_elements_by_xpath("//*[@class='catalog_points_yi']")
                #若本页有橙色点
                if not_sees != [] :
                    not_sees[0].click()
                    self.learning.page_learning()
                    self.driver.refresh()
                    continue
                #若本页没有橙色点
                if not_sees == []:
                    js = "window.scrollBy(0,100)"
                    self.driver.execute_script(js)
                    sleep(0.5)
                    #若滑到底，且没有橙色点，则结束进程
                    total_height=self.driver.execute_script("return document.documentElement.scrollHeight;")
                    current_position=self.driver.execute_script("return window.pageYOffset;")
                    if current_position>=total_height:
                        break
        except Exception as e:
            print (e)
            log.error(e)
            #截图
            self.base.base_get_img()
            #抛异常
            raise


