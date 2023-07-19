from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLogger
import page
from tools.read_yaml import read_yaml
import pytest

log=GetLogger.get_logger()

class TestMpArticle:
    # 1.初始化
    def setup_class(self):
        # 1.获取driver
        driver=GetDriver.get_web_driver(page.url_mp)
        # 2.获取统一入口类对象
        self.page_in=PageIn(driver)
        # 3.获取PageMpLogin对象并调用成功登录方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 4.获取PageMpArticle对象
        self.article=self.page_in.page_get_PageMpArticle()

    # 2.结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_web_driver()

    # 3.测试发布文章方法
    @pytest.mark.parametrize("title,content,expect",read_yaml("mp_article.yaml"))
    def test_mp_article(self,title,content,expect):
        # 1.调用发布文章业务方法
        self.article.page_mp_article(title,content)
        # 2.查看断言信息
        try:
            assert self.article.page_get_info()==expect
        except Exception as e:
            # 日志
            log.error("断言失败，错误信息为：{}".format(e))
            # 截图
            self.article.base_get_img()