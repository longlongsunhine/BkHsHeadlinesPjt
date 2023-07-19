# from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
import allure
from config import BASE_PATH, CURRENT_TIME
import os
from tools.get_log import GetLogger
# from appium.webdriver.webdriver import WebDriver

log = GetLogger.get_logger()


class Base(object):
    # 初始化 方法封装
    def __init__(self, driver):
        log.info("正在初始化driver：{}".format(driver))
        self.driver = driver

    # 查找元素 方法封装
    def base_find(self, loc, timeout=30, poll=0.5):
        # 参数说明
        """
        :param loc:格式为列表或元组  内容：元素定位信息使用by类
        :param timeout:查找元素超时时间，默认：30s，30秒去检测一遍，看元素存不存在
        :param poll: 查找元素频率，默认：0.5s
        :return: 元素
        """
        log.info("正在查找元素：{}".format(loc))
        el = (WebDriverWait(self.driver,
                            timeout=timeout,
                            poll_frequency=poll).until(lambda x: x.find_element(*loc)))
        return el

    # 查找元素集 方法封装
    def base_find_elements(self, loc, timeout=30, poll=0.5):
        # 参数说明
        """
        :param loc:格式为列表或元组  内容：元素定位信息使用by类
        :param timeout:查找元素超时时间，默认：30s，30秒去检测一遍，看元素存不存在
        :param poll: 查找元素频率，默认：0.5s
        :return: 元素
        """
        log.info("正在查找元素：{}".format(loc))
        els = (WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_elements(*loc)))
        return els

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc: 元素定位信息
        :param value: 输入的内容
        """
        # 1.获取元素
        el = self.base_find(loc)
        # 2.清空操作
        log.info("正在对：{} 元素执行清空操作！".format(loc))
        # el.clear()
        el.send_keys(Keys.CONTROL, "a")
        el.send_keys(Keys.BACKSPACE)
        # 3.输入操作
        log.info("正在对：{} 元素执行输入：{} 操作！".format(loc, value))
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        # 获取元素并点击
        log.info("正在对：{} 元素执行点击操作！".format(loc))
        self.base_find(loc).click()

    # 获取 元素文本
    def base_get_text(self, loc):
        """
        :param loc:元素定位信息
        :return: 元素的文本内容
        """
        text = self.base_find(loc).text
        log.info("正在对：{} 元素获取文本操作！获取的文本值为：{}".format(loc, text))
        return text

    # 截图
    def base_get_img(self):
        img_path = os.path.join(BASE_PATH, "image", CURRENT_TIME + ".png")
        # 1.调用截图方法
        log.error("断言出错，正在执行截图操作")
        self.driver.get_screenshot_as_file(img_path)
        # 2.调用图片写入报告方法
        self.__base_write_img(img_path)

    # 将图片写入报告方法（私有）
    def __base_write_img(self, img_path):
        # 调用allure.attach附加方法
        #  allure.attach.file("图片路径","图片类型")
        log.error("断言出错，正在将错误图片写入allure报告！")
        allure.attach.file(img_path, attachment_type=allure.attachment_type.PNG)
