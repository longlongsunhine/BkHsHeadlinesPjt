import page
from base.app_base import AppBase
from time import sleep
from tools.get_log import GetLogger

log=GetLogger.get_logger()

class PageAppLogin(AppBase):

    # 1.点击 我的/未登 菜单
    def page_click_my(self):
        self.base_click(page.app_my)

    # 2.点击 ... 更多登录方式
    def page_click_more_login_methods(self):
        self.base_click(page.app_more_login_methods)

    # 3.点击 密码登录
    def page_click_password_login(self):
        self.base_click(page.app_password_login)

    # 4.输入手机号
    def page_input_phone(self,phone):
        self.base_input(page.app_phone,phone)

    # 5.输入密码
    def page_input_pwd(self,pwd):
        self.base_input(page.app_pwd,pwd)

    # 6.勾选协议
    def page_click_agreement(self):
        self.base_click(page.app_agreement)

    # 7.点击登录
    def page_click_login_btn(self):
        # 建议等待1-2秒
        sleep(1)
        self.base_click(page.app_login_btn)

    # 8.自动保存账号密码 点击取消
    def page_click_save_account_number_cancel_btn(self):
        sleep(1)
        # 判断 自动保存账号密码 弹窗是否出现
        if self.app_base_is_exist(page.app_save_account_number_cancel_btn):
            self.base_click(page.app_save_account_number_cancel_btn)

    # 9.获取昵称
    def page_get_nickname(self):
        # 1.点击 我的
        self.page_click_my()
        # 2.获取昵称
        return self.base_get_text(page.app_nickname)

    # 10.组合登录业务方法
    def page_app_login(self,phone,pwd):
        log.info("正在调用登录业务方法！phone: {} pwd: {}".format(phone,pwd))

        self.page_click_my()
        self.page_click_more_login_methods()
        self.page_click_password_login()
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_agreement()
        self.page_click_login_btn()
        self.page_click_save_account_number_cancel_btn()

    # 10.组合登录依赖成功业务方法
    def page_app_login_success(self, phone="13647468101", pwd="123456"):
        log.info("正在调用登录业务方法！phone: {} pwd: {}".format(phone, pwd))

        self.page_click_my()
        self.page_click_more_login_methods()
        self.page_click_password_login()
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_agreement()
        self.page_click_login_btn()
        self.page_click_save_account_number_cancel_btn()

