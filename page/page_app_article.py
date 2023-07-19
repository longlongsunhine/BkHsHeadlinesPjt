from base.app_base import AppBase
import page
from tools.get_log import GetLogger

log=GetLogger.get_logger()

class PageAppArticle(AppBase):
    # 点击 首页
    def page_click_home_page(self):
        self.base_click(page.app_home_page)

    # 1.查找频道
    def page_click_channel(self,click_text):
        # 调用 从右向左滑动方法
        self.app_base_right_swipe_left(page.app_channel_area,click_text)

    # 2.查找文章
    def page_click_article(self,title):
        # 调用从下向上滑动方法
        self.app_base_down_swipe_up(page.app_article_area,title)

    # 3.查找文章业务方法
    def page_app_article(self,click_text,title):
        log.info("正在调用查看文章业务方法 类别：{} 文章标题：{}".format(click_text,title))

        self.page_click_home_page()
        # 1.调用查找频道
        self.page_click_channel(click_text)
        # 2.调用查找文章
        self.page_click_article(title)