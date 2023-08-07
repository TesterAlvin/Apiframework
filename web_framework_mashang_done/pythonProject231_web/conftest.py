import json

import pytest
from selenium.webdriver import Chrome

from commons.driver import get_webdriver
from commons.pom import DealPage, AdminLoginPage
from commons.utils import img1code


# 匿名驱动
@pytest.fixture
def anonymous_driver():
    yield get_webdriver()


# 前台登录页面的驱动前置
@pytest.fixture(scope='session')
def user_driver():
    driver = get_webdriver()
    driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')

    page = DealPage(driver)
    msg = page.login("admin", "msjy123")
    assert msg == "成功登录"
    yield driver


# 后台登录页面的驱动前置
@pytest.fixture(scope='session')
def admin_driver():
    driver = get_webdriver()
    driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
    # 加载cookie
    with open("data/admin_cookies.json") as f:
        _data = f.read()
        if _data:
            cookies = json.loads(_data)
        else:
            cookies = []
    for cookie in cookies:
        driver.add_cookie(cookie)
    # 刷新页面
    driver.refresh()
    # 断言登录的结果
    is_logined = driver.title != '码尚金融 - 管理员登录'
    print("是否登录", is_logined)
    # 判断是否登录成功，如果没有（说明cookies无效）
    if not is_logined:
        # 实例化一个后台的登录页面的页面对象
        page = AdminLoginPage(driver)
        # 识别验证码
        page.save_img("code.png")
        code = img1code('code.png')
        # 执行登录用例
        msg = page.login("admin", "msjy123", code)
        # 断言是否登录成功
        assert msg == "登录成功"

    yield driver
    # 在后置中去写入保存cookies
    # 后置操作，用例执行完毕之后，才运行的代码
    cookies = driver.get_cookies()
    with open("data/admin_cookies.json", "w") as f:
        f.write(json.dumps(cookies))


@pytest.fixture
def clear_deal_page(user_driver):
    user_driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
