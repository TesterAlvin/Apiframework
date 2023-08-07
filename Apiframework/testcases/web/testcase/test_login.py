import re
import allure
import requests

@allure.epic("项目名称：码尚教育B2C商城接口自动化测试")
@allure.feature("模块名称：用户管理模块测试用例")
class TestLogin:

    token = ""
    access_token = ""
    csrf_token = ""
    sess = requests.session()

    # 登陆测试用例
    def test_login_b2c(self):
        url = "http://101.34.221.219:8010/api.php?s=user/login"
        params = {
            "application":"app",
            "application_client_type":"h5"
        }
        data = {
            "accounts": "baili",
            "pwd": "baili123",
            "type": "username"
        }
        res = TestLogin.sess.request(method="post",url=url,json=data,params=params)
        result = res.json()
        TestLogin.token = result["data"]["token"]
        print(TestLogin.token)

    # 订单列表接口
    def test_order_list(self):
        url = "http://101.34.221.219:8010/api.php?s=order/index"
        params = {
            "application": "app",
            "application_client_type": "h5",
            "token": TestLogin.token
        }
        data = {
            "page": 1,
            "keywords": "",
            "status": "-1",
            "is_more": 1
        }
        res = TestLogin.sess.request(method="post", url=url, json=data, params=params)
        print(res.json())

    # 微信公众号获得access_token接口
    def test_get_access_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": "wx8a9de038e93f77ab",
            "secret": "8326fc915928dee3165720c910effb86"
        }
        res = TestLogin.sess.request(method="get", url=url,params=params)
        result = res.json()
        TestLogin.access_token = result["access_token"]
        print(TestLogin.access_token)

    # 微信公众号文件上传接口
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
        params = {
            "access_token": TestLogin.access_token
        }
        data = {
            "media": open(r"E:\shu.jpg",mode="rb")
        }
        res = TestLogin.sess.request(method="post", url=url, files=data, params=params)
        result = res.json()
        print(result)

    #访问phpwind首页接口
    def test_phpwind_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = TestLogin.sess.request(method="get", url=url,)
        result = res.text
        TestLogin.csrf_token  = re.search('name="csrf_token" value="(.*?)"',result)[1]
        print(TestLogin.csrf_token)


    #登陆phpwind
    def test_login_phpwind(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        headers = {
            "Accept":"application/json, text/javascript, /; q=0.01",
            "X-Requested-With":"XMLHttpRequest"
        }
        data = {
            "username": "baili",
            "password": "baili123",
            "csrf_token": TestLogin.csrf_token,
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        res = TestLogin.sess.request(method="post", url=url,data=data,headers=headers)
        print(res.json())