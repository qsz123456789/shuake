from time import sleep

import page
from base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# 播放键所在iframe
begin_iframe = By.CLASS_NAME, "ans-attach-online"
# 开始播放按钮
begin = By.XPATH, "//button[@class='vjs-big-play-button']"
# 已经播放时间
current_time = By.CLASS_NAME, "vjs-current-time-display"
# 总时间
duration_time = By.CLASS_NAME, "vjs-duration-display"
#重播
resee=By.CLASS_NAME,"vjs-paused"
# 返回课程按钮
return_button = By.CSS_SELECTOR, "#contentFocus"


class PageLearning(Base):
    def __page_play(self):
        # 点击播放按钮
        self.base_click(begin)

    # 让视频播放完
    def __page_diagnose(self):
        while 1:
            sleep(1)
            if self.base_get_text(current_time) == self.base_get_text(duration_time):
            #print("当前播放状态：",resee)
            #if resee.__getattribute__('title')=="重播":
               print("视频已播放完毕")
               break
    #返回上一个窗口
    def __return_course(self):
        sleep(1)
        # 到返回课程按钮所在的frame
        self.driver.switch_to.default_content()
        # 点击返回课程按钮
        self.base_click(return_button)




    # 组合业务（方便调用使用
    def page_learning(self):
        # 切换到第一层frame
        self.driver.switch_to.frame(0)
        sleep(1)
        # 切换到第一层嵌套的frame
        self.base_switch_frame(begin_iframe)
        self.__page_play()
        self.__page_diagnose()
        self.__return_course()

