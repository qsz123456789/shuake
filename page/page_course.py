from time import sleep

import page
from base.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# 章节按钮
parameterize = By.CSS_SELECTOR, ".zj"


class PageCourse(Base):

    # 组合业务（进入课程
    def page_course(self):
        #切换新窗口
        self.base_switch(1)
        sleep(1)
        self.base_click(parameterize)

