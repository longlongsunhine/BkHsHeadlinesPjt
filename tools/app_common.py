from base.app_base import AppBase
from tools.get_log import GetLogger
import page
from time import sleep

log = GetLogger.get_logger()


class AppCommon(AppBase):
    # 1.检测 个人信息保护指引 弹窗
    def check_personal_infor_pro_guide(self):
        log.info("正在调用检测个人信息保护指引弹窗是否出现方法")
        if self.app_base_is_exist(page.app_personal_infor_agree_btn):
            # 2.出现，点击“同意”按钮
            self.base_click(page.app_personal_infor_agree_btn)
            sleep(1)
            self.base_click(page.app_close_btn)

    # 2.检测红包弹窗
    def check_red_envelope(self):
        # 1.判断红包弹窗是否出现
        log.info("正在调用检测红包弹窗是否出现方法")
        if self.app_base_is_exist(page.app_close_red_envelope_btn):
            # 2.出现，点击关闭按钮
            self.base_click(page.app_close_red_envelope_btn)
