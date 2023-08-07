import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# 实例化一个驱动:http://chromedriver.storage.googleapis.com/index.html
driver = Chrome()

# 1.1访问借款页面：
#
# http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053
driver.get('http://47.107.116.139/fangwei/index.php?ctl=deal&id=24053')
# time.sleep(5)
# 1.2账号密码登录
# 点击登录按钮
driver.maximize_window()
driver.find_element(By.XPATH, '//*[@id="deal-intro"]/div[2]/div[8]/a').click()
time.sleep(1)  # 由于网络以及服务器响应时间不同以及场景不同，一般如果元素交互，有页面提示或者跳转
# 一般情况都会加等待（强制等待，隐式等待，显式等待）
driver.find_element(By.XPATH, '//*[@id="login-email-address"]').send_keys('admin')
driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys('msjy123')
driver.find_element(By.XPATH, '//*[@id="ajax-login-submit"]').click()
time.sleep(2)
msg = driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text
# msg2 = driver.find_element(By.XPATH,'//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]').text
# //*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]
# //*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]
print(msg)  # 打印实际结果
assert msg == "成功登录"
# 点击确定按钮
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()

# input("调式继续：")
# 获取当前可投资余额
money = driver.find_element(By.XPATH,'//*[@id="deal-intro"]/div[2]/div[6]/ul/li[2]/span[2]').text
print(money)
# 1.3输入金额
touzi_money = "10000"
driver.find_element(By.XPATH, '//*[@id="J_BIDMONEY"]').send_keys(touzi_money)
# 1.4点击立即投资
driver.find_element(By.XPATH, '//*[@id="tz_link"]').click()
# 1.5输入支付密码（不同的用户密码也不同，admin，（msjy123））
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="J_bid_password"]').send_keys('msjy123')
# 1.6点击确定
driver.find_element(By.XPATH, '//*[@id="J_bindpassword_btn"]').click()
time.sleep(1)
msg3 = driver.find_element(By.XPATH,'//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').text
print(msg3) # //*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]
assert msg3 == "投标成功！"
assert msg3 == "投标成功！"
# 实际结果的确定信息
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()
# 1.7获取系统提示信息，断言:(投标成功！)
money = driver.find_element(By.XPATH,'//*[@id="deal-intro"]/div[2]/div[6]/ul/li[2]/span[2]').text
print(money)
print(type(money))
# shiji_money = money-int(9,278,900.00)
# 资源回收，关闭驱动
input("调式继续：")
driver.quit()
