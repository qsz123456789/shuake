import logging
import os, json
from time import sleep

from selenium import webdriver
from config import DIR_PATH, HOST
import logging.handlers


class DriverUtil:
    __driver = None

    # 获取驱动对象
    @classmethod
    def get_web_driver(cls):
        if cls.__driver is None:
            cls.__driver = webdriver.Chrome(r"E:\chrome-win64\chromedriver.exe")
            cls.__driver.get(HOST)
            cls.__driver.maximize_window()
        return cls.__driver
    #退出驱动对象
    @classmethod
    def quit_web_driver(cls):
        if cls.__driver:
            sleep(3)
            cls.__driver.quit()
            cls.__driver=None


# 读取数据工具
def read_json(filename, key):
    file_path = DIR_PATH + os.sep + "data" + os.sep + filename
    arrs = []
    with open(file_path, "r", encoding='utf-8') as f:
        for data in json.load(f).get(key):
            arrs.append(tuple(data.values())[0:])
        return arrs


#日志封装
class GetLog:
    __log=None
    @classmethod
    def get_log(cls):
        if cls.__log is None:
            #获取日志器
            cls.__log=logging.getLogger()
            #设置入口级别
            cls.__log.setLevel(logging.INFO)
            #获取处理器
            filename=DIR_PATH +os.sep + "log" +os.sep+"xuexitong.log"
            tf=logging.handlers.TimedRotatingFileHandler(filename=filename,
                                                         when="midnight",
                                                         interval=1,
                                                         backupCount=3,
                                                         encoding="utf-8")
            #获取格式器
            fmt="%(asctime)s %(levelname)s [%(filename)s (%(funcName)s:%(lineno)d)] - %(message)s"
            fm=logging.Formatter(fmt)
            #将格式器添加到处理器
            tf.setFormatter(fm)
            #将处理器添加到日志器
            cls.__log.addHandler((tf))
        return cls.__log

if __name__ == '__main__':
    print(read_json("course.json", "course"))
    GetLog.get_log().info("日志测试")