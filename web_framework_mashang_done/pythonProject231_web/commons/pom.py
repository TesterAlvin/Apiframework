# 通过不同的页面封装不同的类，每个页面类，创建对象都拥有自己的属性（元素）和方法（交互）
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait(self, func):  # func = f
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法                           need_text(默认参数等于False)代表需要获取文本（实际结果）
    def find_element(self, by, value, need_text=False):
        def f(driver):  # 自定义需要等待的元素方法f
            txt = driver.find_element(by, value).text
            if need_text:  # 如果需要实际结果文本内容
                # 将返回文本进行替换（如果出现空格进行替换）
                return txt.replace(" ", "")  # 条件成立返回实际值
            else:
                return True  # 直接成功（没有需要获取的实际结果文本内容）

        self.wait(f)  # 通过self对象，调用类方法触发显式等待
        return self.driver.find_element(by, value)  # 最终返回元素


class DealPage(BasePage):
    btn_login = By.XPATH, '//*[@id="deal-intro"]/div[2]/div[8]/a'
    # 定位用户名元素  #          //*[@id="login-email-address"]
    ipt_username = (By.XPATH, '//*[@id="login-email-address"]')
    # 定位密码元素
    ipt_password = (By.XPATH, '//*[@id="login-password"]')
    # 点击登录按钮
    btn_login_submit = (By.XPATH, '//*[@id="ajax-login-submit"]')
    # 获取登录的详细信息
    txt_login_msg = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[2]')
    # 点击确定按钮
    btn_login_ok = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[3]/input[1]')
    # 输入金额             # //*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]
    ipt_money = (By.XPATH, '//*[@id="J_BIDMONEY"]')
    # 立即投资
    btn_deal_submit = (By.XPATH, '//*[@id="tz_link"]')
    # 支付密码
    ipt_pay_password = (By.XPATH, '//*[@id="J_bid_password"]')
    # 确定按钮
    btn_pay_submit = (By.XPATH, '//*[@id="J_bindpassword_btn"]')
    # 投标成功的提示信息
    # //*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]
    txt_deal_msg = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[2]')
    # 定位确定 //*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]
    btn_pay_submit2 = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[3]/input[1]')

    # 登录流程用例
    def login(self, username, password):
        # 通过self对象本身调用定位元素的方法find_element
        # 参数信息直接通过self.类属性（加上*进行元组解包）然后.click()方法完成操作
        # 点击登录

        self.find_element(*self.btn_login).click()
        # input("开始进行登录流程用例：")
        # 输入账号
        self.find_element(*self.ipt_username).send_keys(username)
        # 输入密码
        self.find_element(*self.ipt_password).send_keys(password)
        # 点击登录
        self.find_element(*self.btn_login_submit).click()
        # 获取登录成功的实际结果，触发显式等待
        msg = self.find_element(*self.txt_login_msg, need_text=True).text

        self.find_element(*self.btn_login_ok).click()

        return msg

    # 支付
    def pay(self, money, pay_password):
        # 输入投资金额
        self.find_element(*self.ipt_money).send_keys(money)
        # 点击立即投资
        self.find_element(*self.btn_deal_submit).click()
        # 输入支付密码
        self.find_element(*self.ipt_pay_password).send_keys(pay_password)
        # 点击确定按钮
        self.find_element(*self.btn_pay_submit).click()
        # 获取实际结果：文本内容
        # input("获取实际文本内容：")
        return self.find_element(*self.txt_deal_msg).text


class AdminLoginPage(BasePage):
    ipt_username = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input')
    # 定位密码元素
    ipt_password = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input')
    # 验证码图片识别
    img_code = (By.XPATH, '//*[@id="verify"]')
    # 验证码
    ipt_code = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input')
    # 点击登录按钮
    btn_login_submit = (By.XPATH, '//*[@id="login_btn"]')
    txt_login_msg = (By.XPATH, '//*[@id="login_msg"]')

    # 登录流程用例
    def login(self, username, password, code):
        # 输入账号
        self.find_element(*self.ipt_username).send_keys(username)
        # 输入密码
        self.find_element(*self.ipt_password).send_keys(password)
        # 输入验证码
        self.find_element(*self.ipt_code).send_keys(code)
        # 点击登录
        self.find_element(*self.btn_login_submit).click()
        # 获取登录成功的实际结果，触发显式等待
        msg = self.find_element(*self.txt_login_msg, need_text=True).text
        return msg

    # 处理验证码方法
    def save_img(self, path):
        el = self.find_element(*self.img_code)
        el.screenshot(path)

class XZ(BasePage):
    pass
    # 元素：类属性
    # 用例：方法
    #
class A_Page:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, func):  # func = f
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法                           need_text(默认参数等于False)代表需要获取文本（实际结果）
    def find_element(self, by, value, need_text=False):
        def f(driver):  # 自定义需要等待的元素方法f
            txt = driver.find_element(by, value).text
            if need_text:  # 如果需要实际结果文本内容
                return txt  # 条件成立返回实际值
            else:
                return True  # 直接成功（没有需要获取的实际结果文本内容）

        self.wait(f)  # 通过self对象，调用类方法触发显式等待
        return self.driver.find_element(by, value)  # 最终返回元素


class B_Page:
    pass

    def __init__(self, driver):
        self.driver = driver

    def wait(self, func):  # func = f
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法                           need_text(默认参数等于False)代表需要获取文本（实际结果）
    def find_element(self, by, value, need_text=False):
        def f(driver):  # 自定义需要等待的元素方法f
            txt = driver.find_element(by, value).text
            if need_text:  # 如果需要实际结果文本内容
                return txt  # 条件成立返回实际值
            else:
                return True  # 直接成功（没有需要获取的实际结果文本内容）

        self.wait(f)  # 通过self对象，调用类方法触发显式等待
        return self.driver.find_element(by, value)  # 最终返回元素


class C_Page:
    pass

    def __init__(self, driver):
        self.driver = driver

    def wait(self, func):  # func = f
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法                           need_text(默认参数等于False)代表需要获取文本（实际结果）
    def find_element(self, by, value, need_text=False):
        def f(driver):  # 自定义需要等待的元素方法f
            txt = driver.find_element(by, value).text
            if need_text:  # 如果需要实际结果文本内容
                return txt  # 条件成立返回实际值
            else:
                return True  # 直接成功（没有需要获取的实际结果文本内容）

        self.wait(f)  # 通过self对象，调用类方法触发显式等待
        return self.driver.find_element(by, value)  # 最终返回元素


class D_Page:
    pass

    def __init__(self, driver):
        self.driver = driver

    def wait(self, func):  # func = f
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法                           need_text(默认参数等于False)代表需要获取文本（实际结果）
    def find_element(self, by, value, need_text=False):
        def f(driver):  # 自定义需要等待的元素方法f
            txt = driver.find_element(by, value).text
            if need_text:  # 如果需要实际结果文本内容
                return txt  # 条件成立返回实际值
            else:
                return True  # 直接成功（没有需要获取的实际结果文本内容）

        self.wait(f)  # 通过self对象，调用类方法触发显式等待
        return self.driver.find_element(by, value)  # 最终返回元素


class E_Page:
    pass

    def __init__(self, driver):
        self.driver = driver

    def wait(self, func):  # func = f
        return WebDriverWait(self.driver, 5).until(func)

    # 重写定位元素的方法                           need_text(默认参数等于False)代表需要获取文本（实际结果）
    def find_element(self, by, value, need_text=False):
        def f(driver):  # 自定义需要等待的元素方法f
            txt = driver.find_element(by, value).text
            if need_text:  # 如果需要实际结果文本内容
                return txt  # 条件成立返回实际值
            else:
                return True  # 直接成功（没有需要获取的实际结果文本内容）

        self.wait(f)  # 通过self对象，调用类方法触发显式等待
        return self.driver.find_element(by, value)  # 最终返回元素
