from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep
from tools.get_log import GetLogger
from tools.read_yaml import read_yaml
import pytest

log=GetLogger.get_logger()

class TestAppLogin:
    # 1.初始化
    def setup_class(self):
        # 1.获取driver
        driver=GetDriver.get_app_driver()
        # 2.通过统一入口类对象获取PageAppLogin对象
        self.pageIn=PageIn(driver)
        self.login=self.pageIn.page_get_PageAppLogin()
        self.common=self.pageIn.page_get_AppCommon()

    # 2.结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_app_driver()

    # 3.app登录业务测试方法
    @pytest.mark.parametrize("phone,pwd,expect",read_yaml("app_login.yaml"))
    def test_app_login(self,phone,pwd,expect):
        sleep(1)
        # 点击 同意个人信息保护指引
        self.common.check_personal_infor_pro_guide()
        # 检测是否有红包弹窗，如果有点击取消
        self.common.check_red_envelope()
        # 调用app登录业务方法
        self.login.page_app_login(phone,pwd)
        try:
            # 断言
            assert self.login.page_get_nickname()==expect
        except Exception as e:
            # 日志
            log.error("断言失败，错误信息：{}".format(e))
            # 截图
            self.login.base_get_img()
            # 抛异常
            raise
