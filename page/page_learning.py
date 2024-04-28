from time import sleep

import page
from base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
#任务完成提示栏所在iframe
task_finish_iframe=By.ID,"iframe"
# 播放键,时间所在iframe
begin_iframe = By.CLASS_NAME, "ans-attach-online"
# 开始播放按钮
begin = By.XPATH, "//button[@class='vjs-big-play-button']"
# 已经播放时间
current_time = By.CLASS_NAME, "vjs-current-time-display"
# 总时间
duration_time = By.CLASS_NAME, "vjs-duration-display"
#章节测验按钮
chapter_quiz=By.CSS_SELECTOR,"[title='章节测验']"
# 返回课程按钮
return_button = By.CSS_SELECTOR, "#contentFocus"


class PageLearning(Base):
    def __page_play(self):
        # 切换到第一层frame
        self.driver.switch_to.frame(0)
        sleep(1)
        # 切换到第一层嵌套的frame
        self.base_switch_frame(begin_iframe)
        # 点击播放按钮
        self.base_click(begin)

    # 让视频播放完
    def __page_diagnose(self):
        # 判断视频播放完没
        while 1:
            sleep(3)
            self.base_default_frame()
            # 切换到第一层frame
            self.base_switch_frame(task_finish_iframe)
            sleep(1)
            # 切换到第一层嵌套的frame
            self.base_switch_frame(begin_iframe)
            now = self.base_get_text(current_time)
            all = self.base_get_text(duration_time)
            if now== all:
               break

            self.base_default_frame()
            self.base_switch_frame(task_finish_iframe)
            aria_label = self.driver.find_element(By.CLASS_NAME, "ans-job-icon-clear").get_attribute("aria-label")
            if aria_label == "任务点已完成":
                break

    def __chapter_quiz(self):
        if chapter_quiz:
            self.base_click(chapter_quiz)
    #返回上一个窗口
    def __return_course(self):
        sleep(1)
        # 到返回课程按钮所在的frame
        self.driver.switch_to.default_content()
        # 点击返回课程按钮
        self.base_click(return_button)

    # 组合业务（方便调用使用
    def page_learning(self):
        self.__page_play()
        self.__page_diagnose()
        self.base_default_frame()
        self.__chapter_quiz()
        self.__return_course()

