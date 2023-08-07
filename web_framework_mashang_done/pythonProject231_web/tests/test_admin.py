import pytest
from selenium.webdriver.common.by import By
import allure
from commons.pom import AdminLoginPage


@pytest.mark.parametrize("username,password,code,assert_msg",
                         [["", "", "", "管理员帐号不能为空"],
                          ["admin", "", "", "管理员密码不能为空"],
                          ["admin", "msjy123", "", "验证码不能为空"],
                          ["admin", "msjy123", "6666", "验证码错误"],
                          ["", "msjy123", "2912", "管理员帐号不能为空"], ])
@allure.step("我是测试步骤001")
def test_admin_login_1(anonymous_driver, username, password, code, assert_msg):
    anonymous_driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
    page = AdminLoginPage(anonymous_driver)
    msg = page.login(username=username, password=password, code=code)
    # 管理员帐号不能为空
    allure.attach("进行断言","对预期结果和实际结果断言")
    assert msg == assert_msg


def test_admin_new_deal(admin_driver):
    # 隐式等待
    admin_driver.implicitly_wait(5)
    iframe = admin_driver.find_element(By.XPATH, '/html/frameset/frame[1]')
    admin_driver.switch_to.frame(iframe)
    # 断言 登录账户:admin
    assert "登录账户:admin" in admin_driver.page_source
    # print(admin_driver.page_source)
