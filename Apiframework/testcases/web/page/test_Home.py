# coding = utf-8

from selenium.webdriver.common.by import By
import time

from apiauto.Apiframework.testcases.web.Base.Base import Base


'''# 继承Base,可以直接使用Base中的self.driver'''
class TestHome(Base):
    '''元素定位方式和属性值'''
    username_input = (By.NAME, 'username')
    pwassword_input = (By.NAME, 'password')
    login_click = (By.XPATH,'//*[@id="app"]/div/form/button')

    '''元素操作方法'''
    '''调用base的Base类中封装的元素定位方法'''
    # 用户名框输入方法
    def input_username(self, value):
        self.ele_sendkeys(TestHome.username_input, value)

    # 密码框输入方法
    def input_pwassword(self, value):
        self.ele_sendkeys(TestHome.pwassword_input, value)

    # 按钮点击方法
    def click_login(self):
        self.ele_click(TestHome.login_click)

    '''业务操作'''
    def login(self, value):
        self.input_username(value)
        self.input_pwassword(value)
        time.sleep(2)
        self.click_login()
