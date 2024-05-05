#用于执行script中所有文件
import os
import unittest
from htmltestreport import HTMLTestReport

from config import DIR_PATH

suite = unittest.defaultTestLoader.discover("./script")
file_path = DIR_PATH + os.sep + "report" + os.sep + "自动刷课.html"
HTMLTestReport(file_path).run(suite)