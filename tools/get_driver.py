# from selenium import webdriver
# 导包
from appium import webdriver
import yaml
import os
from tools.get_log import GetLogger
from time import sleep
from config import BASE_PATH

log = GetLogger.get_logger()


class GetDriver():
    # 1.声明变量
    __web_driver = None

    # 声明app中driver变量
    __app_driver = None

    # 2.获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断是否为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver = None

    # 获取app应用driver
    @classmethod
    def get_app_driver(cls):
        # 判断__app_driver 为空
        if cls.__app_driver is None:
            # 设置启动
            desired_cap_path = os.path.join(BASE_PATH, "config", "desired_cap.yaml")
            with open(desired_cap_path, "r", encoding="utf-8") as file:
                data = yaml.load(file, Loader=yaml.FullLoader)

            base_path = os.path.dirname(os.path.dirname(__file__))
            # os.path.join()：用于拼接路径
            app_path = os.path.join(base_path, "app", data["appname"])

            desired_cap = {}
            desired_cap["platformName"] = data["platformName"]
            desired_cap["platformVersion"] = data["platformVersion"]
            desired_cap["deviceName"] = data["deviceName"]
            desired_cap["app"] = app_path
            desired_cap["appPackage"] = data["appPackage"]
            desired_cap["appActivity"] = data["appActivity"]
            desired_cap["noReset"] = data["noReset"]
            desired_cap["unicodeKeyboard"] = data["unicodeKeyboard"]
            desired_cap["resetKeyboard"] = data["resetKeyboard"]
            desired_cap["automationName"] = data["automationName"]

            log.info("start app....")
            cls.__app_driver = webdriver.Remote(f'http://{data["ip"]}:{data["port"]}/wd/hub',
                                                desired_capabilities=desired_cap)
            cls.__app_driver.implicitly_wait(8)

        # 返回cls.__app_driver
        return cls.__app_driver

    # 退出app应用driver
    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None


if __name__ == '__main__':
    GetDriver.get_app_driver()
    sleep(1)
    GetDriver.quit_app_driver()
