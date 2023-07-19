from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLogger
import pytest
from tools.read_yaml import read_yaml

log=GetLogger.get_logger()


class TestAppArticle:
    # 1.初始化
    def setup_class(self):
        # 1.获取driver
        driver=GetDriver.get_app_driver()
        # 2.获取统一入口类对象
        self.page_in=PageIn(driver)
        # 3.通过统一入口类获取AppCommon对象
        self.app_common=self.page_in.page_get_AppCommon()
        self.app_common.check_personal_infor_pro_guide()
        self.app_common.check_red_envelope()
        # 4.调用登录方法
        self.page_in.page_get_PageAppLogin().page_app_login_success()
        # 5.获取发布文章页面对象
        self.article=self.page_in.page_get_PageAppArticle()

    # 2.结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 3.发布文章测试方法
    @pytest.mark.parametrize("click_text,title",read_yaml("app_article.yaml"))
    def test_app_article(self,click_text,title):
        try:
            # 发布文章业务方法
            self.article.page_app_article(click_text,title)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            # 抛异常
            raise

