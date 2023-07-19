from selenium.common import NoSuchElementException
from base.base import Base
from tools.get_log import GetLogger
from selenium.webdriver.common.by import By
from time import sleep

log = GetLogger.get_logger()


class AppBase(Base):
    # 1.查找页面是否存在指定元素
    def app_base_is_exist(self, loc):
        log.info("正在调用查找页面是否存在指定元素：{} 方法".format(loc))
        try:
            # 1.调用查找方法
            self.base_find(loc, timeout=3)
            # 2.输入信息
            log.info("找到：{} 元素！".format(loc))
            # 3.返回True
            return True
        except:
            # 1.输出信息
            log.info("没有找到：{} 元素！".format(loc))
            # 2.返回False
            return False

    # 2.滑动方法封装
    def app_base_swip(self, start_x, start_y, end_x, end_y, duration=500):
        log.info("正在调用滑动方法！start_x:{} start_y:{} end_x:{} end_y:{} duration:{}".format(start_x, start_y, end_x,
                                                                                               end_y, duration))
        # 1.获取屏幕尺寸
        size = self.driver.get_window_size()
        log.info("正在获取屏幕尺寸：{}".format(size))
        # 2.设置滑动起始坐标
        start_x = size['width'] * start_x
        start_y = size['height'] * start_y
        end_x = size['width'] * end_x
        end_y = size['height'] * end_y
        # 3.调用swip滑动方法
        log.info("正在执行滑动操作！")
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    # 3.从右向左滑动屏幕，并查找指定元素
    def app_base_right_swipe_left(self,loc_area,click_text):
        log.info("正在调用从右向左滑动方法！")
        """
        :param loc_area: 区域元素定位信息
        :param click_text: 点击文本
        """
        # 1.查找区域元素
        el=self.base_find(loc_area)
        # 2.获取区域元素的位置 y坐标点
        y=el.location.get("y")
        # 3.获取区域元素宽高
        width=el.size.get("width")
        height=el.size.get("height")
        # 4.计算 start_x, start_y, end_x, end_y
        start_x=width*0.8
        start_y=y+height*0.5
        end_x=width*0.2
        end_y=start_y
        # 组合频道元素配置信息
        # loc=By.XPATH,"//*[contains(@content-desc,'{}')]".format(click_text)
        loc = By.XPATH, "//*[@class='android.widget.HorizontalScrollView']//*[contains(@content-desc,'{}')]".format(click_text)
        # 5.循环操作
        while True:
            # 1.获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2.捕获异常
            try:
                # 1.查找元素
                self.base_find(loc,timeout=3)
                # sleep(1)
                # el2=el.find_element(*loc)
                # 2.输出提示信息
                log.info("找到：{} 元素了！".format(loc))
                # 3.点击元素
                self.base_click(loc)
                # 4.跳出循环
                break
                # 3.处理异常
            except:
                # 1.输出提示信息
                log.info("未找到：{} 元素".format(loc))
                # 2.滑动屏幕
                self.driver.swipe(start_x,start_y,end_x,end_y,duration=500)
                # 4.判断是否为最后一页
                if page_source==self.driver.page_source:
                    # 1.输出提示信息
                    log.error("滑动最后一屏幕，没有找到元素")
                    # 2.抛出未找到异常
                    raise NoSuchElementException

    # 4.从下向上滑动屏幕，并在指定区域内查找指定元素
    def app_base_down_swipe_up(self, loc_area, click_text):
        log.info("正在调用从下向上滑动方法！")
        """
        :param loc_area: 区域元素定位信息
        :param click_text: 点击文本
        """
        # 1.查找区域元素
        el = self.base_find(loc_area)
        # 2.获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4.计算 start_x, start_y, end_x, end_y
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height*0.2
        # 组合频道元素配置信息
        loc = By.XPATH, "//*[@resource-id='com.ss.android.article.news:id/ao']//*[contains(@content-desc,'{}')]".format(
            click_text)
        # 5.循环操作
        while True:
            # 1.获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2.捕获异常
            try:
                sleep(1)
                # 1.查找元素
                self.base_find(loc, timeout=3)
                sleep(1)
                # 2.输出提示信息
                log.info("找到：{} 元素了！".format(loc))
                # 3.点击元素
                self.base_click(loc)
                # 4.跳出循环
                break
                # 3.处理异常
            except:
                # 1.输出提示信息
                log.info("未找到：{} 元素".format(loc))
                # 2.滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=300)
                # 4.判断是否为最后一页
                if page_source == self.driver.page_source:
                    # 1.输出提示信息
                    log.error("滑动最后一屏幕，没有找到元素")
                    # 2.抛出未找到异常
                    raise NoSuchElementException
