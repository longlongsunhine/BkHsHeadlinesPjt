from selenium.webdriver.common.by import By

"""以下数据为自媒体、后台管理url"""
# 自媒体url
url_mp = "http://pc-toutiao-python.itheima.net/#/login"
# 后台管理url
url_mis = "http://heima-admin-java.itheima.net/#/login"

"""以下数据为自媒体模块配置数据"""
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder=请输入手机号]")
# 验证码
mp_code = (By.CSS_SELECTOR, '[placeholder="验证码"]')
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, ".el-button--primary")
# 昵称
mp_nickname = (By.CSS_SELECTOR, ".user-name")

# 发布文章页面元素
# 内容管理
mp_content_manage = By.XPATH, "//*[text()='内容管理']/.."
# 发布文章
mp_publish_article = By.XPATH, "//*[contains(text(),'发布文章')]"
# 文章标题
mp_title = By.CSS_SELECTOR, '[placeholder="文章名称"]'
# iframe
mp_iframe = By.CSS_SELECTOR, "#publishTinymce_ifr"
# 文章内容，定位到body，勿定位到<p></p>标签
mp_content = By.CSS_SELECTOR, "#tinymce"
# 封面
mp_cover = By.XPATH, "//*[text()='自动']"
# 发表
mp_submit = By.XPATH, "//*[text()='发表']/.."
# 结果
mp_result = By.XPATH, "//*[contains(text(),'新增文章成功')]"

"""以下配置信息为后台管理元素"""
# 用户名
mis_username = By.XPATH, '//*[@id="app"]/div/div/div[2]/form/div[2]/div/div/input'
# 密码
mis_pwd = By.XPATH, "//*[@type='password']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, ".el-button"
# 昵称
mis_nickname = By.CSS_SELECTOR, ".user-name"

"""以下配置信息为app元素"""
# 个人信息保护指引 弹窗 同意按钮
app_personal_infor_agree_btn = By.ID, "com.ss.android.article.news:id/ek0"
# 关闭按钮
app_close_btn = By.ID, "com.ss.android.article.news:id/g4f"
# 关闭红包弹窗按钮
app_close_red_envelope_btn = By.ID, "com.ss.android.article.news:id/bkp"
# 我的/未登录按钮
app_my = By.XPATH,"//*[@resource-id='com.ss.android.article.news:id/cxt' and @text='未登录' or @text='我的']"
# 更多登录方式
app_more_login_methods = By.XPATH, "//*[@content-desc='更多登录方式']"
# 密码登录
app_password_login = By.XPATH, "//*[@text='密码登录']"
# 手机号
app_phone = By.ID, "com.ss.android.article.news:id/hx"
# 密码
app_pwd = By.ID, "com.ss.android.article.news:id/i6"
# 协议
app_agreement = By.ID, "com.ss.android.article.news:id/exc"
# 登录按钮
app_login_btn = By.ID, "com.ss.android.article.news:id/alq"
# 自动保存账号密码 取消按钮
app_save_account_number_cancel_btn = By.XPATH, "//*[@resource-id='android:id/button2' and @text='取消']"
# 昵称
app_nickname = By.ID, "com.ss.android.article.news:id/e7l"
# 区域频道
app_channel_area=By.ID,"com.ss.android.article.news:id/ap7"
# 首页
app_home_page=By.XPATH,"//*[@resource-id='com.ss.android.article.news:id/cxt' and @text='首页']"
# 文章区域
app_article_area=By.ID,"com.ss.android.article.news:id/ao"
