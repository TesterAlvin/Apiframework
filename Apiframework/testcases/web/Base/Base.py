# coding = utf-8

class Base:
    '''第一步：构造方法初始化浏览器    让页面类，用例类都公用这一个浏览器'''
    def __init__(self, driver):
        self.driver = driver

    '''第二步：封装常见的操作'''
    # 元素定位
    def local_ele(self, loc):
        return self.driver.find_element(*loc)

    # 发送文本
    def ele_sendkeys(self, loc, value):
        self.local_ele(loc).send_keys(value)

    # 点击
    def ele_click(self, loc):
        self.local_ele(loc).click()

    #关闭浏览器
    def close_browser(self):
        self.driver.quit()
