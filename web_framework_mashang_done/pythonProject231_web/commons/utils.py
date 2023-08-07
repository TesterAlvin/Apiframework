# 获取保存cookies信息
import json
import time
import requests


def save_cookies(driver):
    # 保存cookie信息到本地文件
    cookies = driver.get_cookies()
    with open("../cookies.json", "w") as f:
        f.write(json.dumps(cookies))


def load_cookies(driver):
    # 使用（加载）cookie信息到本地文件
    driver.get('http://47.107.116.139/fangwei/m.php?m=Index&a=index&')
    try:
        with open("../cookies.json") as f:
            cookies = json.loads(f.read())
        # 使用所有cookies信息
        for cookie in cookies:
            driver.add_cookie(cookie)
        else:
            # 刷新缓存
            driver.refresh()
    except:
        print("目前没有已登录的cookies信息，不能直接使用ID")
        pass


def is_login(driver):
    # 通过页面标题判断是否已登录
    if '管理员登录' in driver.title:
        print("需要登录")
        return False
    else:
        print("已登录")
        driver.maximize_window()
        time.sleep(3)
        return True


def img1code(file):
    url2 = "http://upload.chaojiying.net/Upload/Processing.php"

    data = {

        'user': 'javen0921',
        'pass': 'Cen851395',
        'softid': '948409',
        'codetype': '4004',

    }
    files = {"userfile": open(file, "rb")}
    resp = requests.post(url2, data=data, files=files)
    # print(resp.json())
    # print(type(resp.json()))
    res = resp.json()
    print(res)
    # 判断验证码是否识别成功
    if res["err_no"] == 0:
        code = res['pic_str']
        print(f"识别成功:{code}")
        return code
    else:
        print("识别失败")
        return False
