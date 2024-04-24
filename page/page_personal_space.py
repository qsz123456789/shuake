from time import sleep

import page
from base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
'''
以下为web刷课程模块配置信息
'''
# 课程按钮
course_btn = By.XPATH, "//*[@title='课程']"


class PagePersonalSpace(Base):
    # 点击课程按钮
    def __page_click_course_btn(self):
        self.base_click(course_btn)

    # 点击想刷的课
    def __page_click_want_course_btn(self,value):
            want_course_btn = By.XPATH,"//*[contains(@title,'{}')]".format(value)
            self.base_click(want_course_btn)

# 组合业务（方便调用使用
    def page_personal_space(self,value):
        self.__page_click_course_btn()
        sleep(1)
        self.driver.switch_to.frame(0)
        self.__page_click_want_course_btn(value)