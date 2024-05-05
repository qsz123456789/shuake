import os
from datetime import  datetime

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from base import log
from config import DIR_PATH
class Base:
    #初始化方法
    def __init__(self,driver):
        log.info("正在初始化，driver对象：{}".format(driver))
        self.driver=driver
    #查找元素方法
    def base_find(self,loc,timeout=30,poll_frequency=0.5):
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))

    #点击方法
    def base_click(self,loc):
        log.info("正在点击元素：{}".format(loc))
        self.base_find(loc).click()
    #输入方法
    def base_input(self,loc,value):
        log.info("正在调用输入元素方法：{},输入内容：{}".format(loc,value))
        #获取元素
        el = self.base_find(loc)
        #清空
        el.clear()
        #输入
        el.send_keys(value)
    #获取文本方法
    def base_get_text(self,loc):
        log.info("正在调用获取元素信息方法：{}".format(loc))
        return self.base_find(loc).text
    #截图方法
    def base_get_img(self):
        log.info("正在调用截图方法")
        dt=datetime.now()
        time_obj=dt.time()
        img_path=DIR_PATH+os.sep+"img"+"os.sep"+"{}.png".format(time_obj.strftime("%H:%M:%S"))
        self.driver.get_screenshot_as_file("{}.png".format(img_path))
    #切换iframe方法
    def base_switch_frame(self,loc):
        log.info("正在调用切换iframe方法，切换对象：{}".format(loc))
        el=self.base_find(loc)
        self.driver.switch_to.frame(el)
    #恢复默认frame
    def base_default_frame(self):
        self.driver.switch_to.default_content()
    #切换窗口
    def base_switch(self,n):
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[n])
    #判断元素是否可见
    def base_is_displayed(self,loc):
        try:
            self.base_find(loc).is_displayed()
        except NoSuchElementException:
            return False
        return True
    #滚动条滑到底
    def base_scroll(self):
        js="window.scrollTo(0,10000)"
        self.driver.execute_script(js)


