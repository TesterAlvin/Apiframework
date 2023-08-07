import time
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


    def test_wronglogin(self):

        driver.find_element(By.NAME,'username').send_keys('admin')
        driver.find_element(By.NAME,'password').send_keys('wrongpwd')#输出错误密码判断
        #点击登录
        driver.find_element(By.XPATH,'//*[@id="app"]/div/form/button').click()
        #断言错误密码
        time.sleep(2)
        toast=driver.find_element(By.XPATH, '/html/body/div[2]').text
        assert '账号或密码错误' in toast

if __name__ == '__main__':
    pytest.main()
