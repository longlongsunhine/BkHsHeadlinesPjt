import page
from base.web_base import WebBase
from time import sleep
from tools.get_log import GetLogger

log=GetLogger.get_logger()

class PageMpLogin(WebBase):
    # 输入用户名
    def page_input_username(self,username):
        self.base_input(page.mp_username,username)

    # 输入验证码
    def page_input_code(self,code):
        self.base_input(page.mp_code,code)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取昵称封装 ——>测试脚本层断言使用
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 组合登录业务方法封装 ——>测试脚本层调用
    def page_mp_login(self,username,code):
        """提示：调用相同页面操作步骤，跨越面暂不考虑"""
        log.info("正在调用自媒体登录业务，用户名：{} 验证码：{}".format(username,code))
        sleep(1)
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()

    # 组合登录业务方法封装 ——>发布文章依赖使用
    def page_mp_login_success(self, username="12011111111", code="246810"):
        """提示：调用相同页面操作步骤，跨越面暂不考虑"""
        log.info("正在调用自媒体登录业务，用户名：{} 验证码：{}".format(username, code))
        sleep(1)
        self.page_input_username(username)
        self.page_input_code(code)
        self.page_click_login_btn()
