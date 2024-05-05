#整理配置信息
from selenium.webdriver.common.by import By

'''
    一.以下为登录界面配置信息
'''
#用户名
phone=By.ID,"phone"
#密码
pwd=By.ID,"pwd"
#登录按钮
login_btn=By.XPATH,"//*[contains(@type,'button')]"
#昵称
nickname=By.XPATH,"//*[@class='user-name']"

'''
    二.以下为个人空间界面配置信息
'''
# 课程按钮
course_btn = By.XPATH, "//*[@title='课程']"

'''
    三.以下为xxx课程界面配置信息
'''
# 章节按钮
parameterize = By.CSS_SELECTOR, ".zj"

'''
    四.以下为学习界面配置信息
'''
#任务完成提示栏所在iframe
task_finish_iframe=By.ID,"iframe"
# 播放键,时间所在iframe
begin_iframe = By.CLASS_NAME, "ans-attach-online"
# 开始播放按钮
begin = By.XPATH, "//button[@class='vjs-big-play-button']"
#知道了按钮
know_button=By.CLASS_NAME,"writeNote_vid_blue"
#倍速按钮
view_space_button=By.CLASS_NAME,"vjs-playback-rate-value"
# 返回课程按钮
return_button = By.CSS_SELECTOR, "#contentFocus"