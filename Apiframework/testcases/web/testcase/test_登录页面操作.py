from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

# 驱动文件路径
driverfile_path = r'C:\Users\qiyun\chromedriver.exe'
# 启动浏览器
driver = webdriver.Chrome(executable_path=driverfile_path)
# 打开登录页面
driver.get(r'https://jiankangbaoding.cn/test/health/login')
#最大化窗口
driver.maximize_window()
#显示等待，最大等待时间为8秒，超过返回报错
driver.implicitly_wait(8)

class Test_baoding():

    def test_jiaoyan(self):
        assert '健康门户管理后台' in driver.title    #断言为指定title
        assert 'https://jiankangbaoding.cn/test/health/login' == driver.current_url  # 断言为指定url

    def test_login(self):
        #输入账号密码
        driver.find_element(By.NAME,'username').send_keys('admin')
        driver.find_element(By.NAME,'password').send_keys('LPh4XyOovMCf')
        #点击登录
        driver.find_element(By.XPATH,'//*[@id="app"]/div/form/button').click()
        #断言登录后的内容
        title=driver.find_element(By.XPATH,'//*[@id="app"]/div/div[1]/div[1]/a/h1').text
        print(title)
        #断言判断系统标题
        assert title in '健康门户后台管理 '

if __name__ == '__main__':
    pytest.main()
