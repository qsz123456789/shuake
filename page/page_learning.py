from time import sleep

import page
from base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains



class PageLearning(Base):
    def __page_play(self):
        self.base_default_frame()
        # 切换到第一层frame
        self.base_switch_frame(page.task_finish_iframe)
        sleep(1)
        # 切换到第一层嵌套的frame
        self.base_switch_frame(page.begin_iframe)
        # 点击播放按钮
        self.base_click(page.begin)
        sleep(1)
        #点击知道了按钮
        #self.base_click(know_button)
        #sleep(3)
        #把display设置成block，使倍速按钮可见
        #self.driver.find_element(By.CLASS_NAME,"vjs-playback-rate-value").display = 'block'
        #action=ActionChains(self.driver)
        #action.move_to_element(view_space_button)
        #action.click(view_space_button)
    # 让视频播放完
    def __page_diagnose(self):
        # 判断视频播放完没
        while 1:
            sleep(3)
            self.base_default_frame()
            #切换到第一层frame
            self.base_switch_frame(page.task_finish_iframe)
            aria_label = self.driver.find_element(By.CLASS_NAME, "ans-job-icon-clear")
            if aria_label.get_attribute("aria-label") == "任务点已完成":
                break
    #返回上一个窗口
    def __return_course(self):
        sleep(1)
        # 到返回课程按钮所在的frame
        self.driver.switch_to.default_content()
        # 点击返回课程按钮
        self.base_click(page.return_button)

    # 组合业务（方便调用使用
    def page_learning(self):
        self.__page_play()
        self.__page_diagnose()
        self.__return_course()

