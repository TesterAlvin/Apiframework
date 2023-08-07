import time
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

# 驱动文件路径
driverfile_path = r'C:\Users\qiyun\chromedriver.exe'
# 启动浏览器
driver = webdriver.Chrome(executable_path=driverfile_path)
# 打开登录页面
driver.get(r'https://a35.aplcc.net/user/login')
#最大化窗口
driver.maximize_window()
#显示等待，最大等待时间为8秒，超过返回报错
driver.implicitly_wait(8)

class Test_hulianwang():

    def test_jiaoyan(self):
        assert '深圳达实旗云健康科技有限公司' in driver.title    #断言为指定title
        assert 'https://a35.aplcc.net/user/login' == driver.current_url  # 断言为指定url

    def test_login(self):
        #输入账号密码
        driver.find_element(By.ID,'username').send_keys('admin')
        driver.find_element(By.ID,'password').send_keys('das@bch123')
        #点击登录
        driver.find_element(By.XPATH,'//*[@id="formLogin"]/div[4]/div/div/span/button').click()
        #断言登录后的内容
        title=driver.find_element(By.XPATH,'//*[@id="logo"]/a/div/h1').text
        print(title)
        #断言判断系统标题
        assert title in '运维后台 '

    def test_menu(self):
        #校验菜单名称
        menu1=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/aside/div/ul/li[1]/div[1]/span/span/span').text
        menu2=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/aside/div/ul/li[2]/div[1]/span/span/span').text
        menu3=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/aside/div/ul/li[3]/div[1]/span/span/span').text
        menu4=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/aside/div/ul/li[4]/div[1]/span/span/span').text
        menu5=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/aside/div/ul/li[5]/div[1]/span/span/span').text
        menu6=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/aside/div/ul/li[6]/div[1]/span/span/span').text
        menu7=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/aside/div/ul/li[7]/div[1]/span/span/span').text
        menu8=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/aside/div/ul/li[8]/div[1]/span/span/span').text
        # text=driver.find_element(By.XPATH,'//*[@id="app"]/div/section/section/div/header[2]/div/div[2]/span').text
        # print(text)
        # time.sleep(3)
        assert menu1 in '平台统计 '
        assert menu2 in '系统管理 '
        assert menu3 in '商户管理 '
        assert menu4 in '账单管理 '
        assert menu5 in '对账管理 '
        assert menu6 in '互联网医院 '
        assert menu7 in '运维分析 '
        assert menu8 in '基础服务 '

if __name__ == '__main__':
    pytest.main()
