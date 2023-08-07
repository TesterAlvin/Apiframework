# 直接通过导包，使用pom模块的类里面的属性进行直接调用

from commons.pom import DealPage, AdminLoginPage


def test_user_login_ok(driver):
    # driver = Chrome()
    driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')

    page = DealPage(driver)
    msg = page.login("admin", "msjy123")
    assert msg == "成功登录"

    msg = page.pay(100, "msjy123")
    assert msg == "投标成功！"


def test_user_login_fail(driver):
    # driver = Chrome()
    driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')

    page = DealPage(driver)
    msg = page.login("admin", "msjy123456")
    assert msg == "密码错误"


def test_user_deal_ok(user_driver, clear_deal_page):
    # user_driver.refresh()
    # user_driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')

    page = DealPage(user_driver)
    msg = page.pay(100, "msjy123")
    assert msg == "投标成功！"


def test_user_deal_fail(user_driver, clear_deal_page):
    # user_driver.refresh()
    # user_driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')

    page = DealPage(user_driver)
    msg = page.pay(200, "12321321321")
    assert msg == "支付密码错误"


# def test_admin(driver):
#     # 后台登录页用例设计
#     driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
#
#     page = AdminLoginPage(driver)
#     msg = page.login("admin", "msjy123")
#     assert msg == "验证码不能为空"
