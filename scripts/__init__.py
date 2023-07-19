# 不加这个就会出现导包错误，当用例模块运行时，就会自动加载此模块的内容
import sys
import os
sys.path.append(os.getcwd())