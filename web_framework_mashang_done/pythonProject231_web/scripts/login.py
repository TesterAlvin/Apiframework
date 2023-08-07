import time

from selenium import webdriver

from selenium.webdriver.common.by import By

import requests

from commons.utils import save_cookies, load_cookies, is_login

# 创建一个驱动对象
driver = webdriver.Chrome()
# 使用本地记录的cookies信息
load_cookies(driver)
# 刷新页面
driver.refresh()

# 可以开始进行判断是否已经登录
if is_login(driver) is False:
    url = "http://47.107.116.139/fangwei/m.php?m=Public&a=login&"

    # 通过驱动访问页面
    driver.get(url)

    # 页面最大化
    driver.maximize_window()
    # 使用cookies
    load_cookies(driver)
    # 对验证码图片进行截图
    driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot('verify.png')
    # 通过第三方平台识别验证码
    url2 = "http://upload.chaojiying.net/Upload/Processing.php"

    data = {

        'user': 'fzjbatman',
        'pass': '5978627s',
        'softid': '945547',
        'codetype': '4004',

    }
    files = {"userfile": open("../verify.png", "rb")}
    resp = requests.post(url2, data=data, files=files)
    # print(resp.json())
    # print(type(resp.json()))
    res = resp.json()
    # 判断验证码是否识别成功
    if res["err_no"] == 0:
        code = res['pic_str']
        print(f"识别成功:{code}")
    else:
        print("识别失败")

    # 定位元素进行输入内容及操作
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input').send_keys('admin')
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input').send_keys('msjy123')
    driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input').send_keys(code)
    # input()
    driver.find_element(By.XPATH, '//*[@id="login_btn"]').click()
    # 登录成功保存cookies信息
    save_cookies(driver)
    time.sleep(5)
    driver.quit()
