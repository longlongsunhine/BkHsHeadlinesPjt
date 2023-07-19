import os
from time import strftime,localtime,time

# 获取项目根目录路径
BASE_PATH=os.path.dirname(__file__)
# 获取当前时间
CURRENT_TIME=strftime("%Y_%m_%d %H_%M_%S",localtime(time()))
