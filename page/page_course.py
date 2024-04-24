from time import sleep

import page
from base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# 章节按钮
parameterize = By.CSS_SELECTOR, ".zj"


class PageCourse(Base):
    # 滚动条方法(多次滚动）,看到没完成的课程就点击
    def __page_scroll(self):
        # 拖动滑条
        js = "window.scrollBy(0,100)"
        self.driver.execute_script(js)
        sleep(0.5)
        # 查找并点击没观看的视频
        not_sees = self.driver.find_elements_by_xpath("//*[@class='catalog_points_yi']")
        not_sees[0].click()
        sleep(1)

    # 组合业务（方便调用使用
    def page_course(self):
        #切换新窗口
        self.base_switch(1)
        sleep(1)
        self.base_click(parameterize)
        self.driver.switch_to.frame(0)
        self.__page_scroll()