from time import sleep

import page
from base.base import Base
from selenium.webdriver.common.by import By

#操作步骤封装+组合业务方法
class PageLogin(Base):
    #输入用户名
    def __page_phone(self,value):
        self.base_input(page.phone,value)

    #输入密码
    def __page_pwd(self,value):
        self.base_input(page.pwd,value)
    #点击登录按钮
    def __page_click_login_btn(self):
        self.base_click(page.login_btn)
    #获取登录昵称
    def page_get_nickname(self):
        sleep(2)
        return self.base_get_text(page.nickname)

    #组合业务（方便调用使用
    def page_login(self,phone,pwd):
        self.__page_phone(phone)
        self.__page_pwd(pwd)
        self.__page_click_login_btn()
        self.page_get_nickname()
