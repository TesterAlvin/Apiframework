import re
from pathlib import Path

import allure
import pytest
import requests
from apiauto.Apiframework.common.requests_util import Requestsutil
from apiauto.Apiframework.common.yaml_util import YamlUtil

#无论在在哪里执行，获取当前文件的绝对路径
cuurent_path=str(Path(__file__).parent)

@allure.epic("项目名称：码尚教育B2C商城接口自动化测试")
@allure.feature("模块名称：用户管理模块测试用例")
class TestLogin:

    token = ""
    access_token = ""
    csrf_token = ""
    sess = requests.session()

    # 登陆测试用例
    # def test_login_b2c(self):
    #     url = "http://101.34.221.219:8010/api.php?s=user/login"
    #     params = {
    #         "application":"app",
    #         "application_client_type":"h5"
    #     }
    #     data = {
    #         "accounts": "baili",
    #         "pwd": "baili123",
    #         "type": "username"
    #     }
    #     res = TestLogin.sess.request(method="post",url=url,json=data,params=params)
    #     result = res.json()
    #     TestLogin.token = result["data"]["token"]
    #     print(TestLogin.token)

    # 订单列表接口
    # def test_order_list(self):
    #     url = "http://101.34.221.219:8010/api.php?s=order/index"
    #     params = {
    #         "application": "app",
    #         "application_client_type": "h5",
    #         "token": TestLogin.token
    #     }
    #     data = {
    #         "page": 1,
    #         "keywords": "",
    #         "status": "-1",
    #         "is_more": 1
    #     }
    #     res = TestLogin.sess.request(method="post", url=url, json=data, params=params)
    #     print(res.json())

    # 微信公众号获得access_token接口
    # def test_get_access_token(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/token"
    #     params = {
    #         "grant_type": "client_credential",
    #         "appid": "wx8a9de038e93f77ab",
    #         "secret": "8326fc915928dee3165720c910effb86"
    #     }
    #     res = TestLogin.sess.request(method="get", url=url,params=params)
    #     result = res.json()
    #     TestLogin.access_token = result["access_token"]
    #     print(TestLogin.access_token)

    # 微信公众号文件上传接口
    # def test_file_upload(self):
    #     url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg"
    #     params = {
    #         "access_token": TestLogin.access_token
    #     }
    #     data = {
    #         "media": open(r"E:\shu.jpg",mode="rb")
    #     }
    #     res = TestLogin.sess.request(method="post", url=url, files=data, params=params)
    #     result = res.json()
    #     print(result)

    #访问phpwind首页接口
    # def test_phpwind_start(self):
    #     url = "http://47.107.116.139/phpwind/"
    #     res = TestLogin.sess.request(method="get", url=url,)
    #     result = res.text
    #     TestLogin.csrf_token  = re.search('name="csrf_token" value="(.*?)"',result)[1]
    #     print(TestLogin.csrf_token)


    #登陆phpwind
    # def test_login_phpwind(self):
    #     url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    #     headers = {
    #         "Accept":"application/json, text/javascript, /; q=0.01",
    #         "X-Requested-With":"XMLHttpRequest"
    #     }
    #     data = {
    #         "username": "baili",
    #         "password": "baili123",
    #         "csrf_token": TestLogin.csrf_token,
    #         "backurl": "http://47.107.116.139/phpwind/",
    #         "invite": ""
    #     }
    #     res = TestLogin.sess.request(method="post", url=url,data=data,headers=headers)
    #     print(res.json())


    #登录便民服务系统
    def test_login_bm(self):
        url = "https://hynq.halixun.com/test/admin/user/login"
        params = {
                "Accept":"application/json, text/plain, */*",
                "Content-Type:":"application/json;charset=UTF-8"
            }
        data = {
                "password": "LPh4XyOovMCf",
                "username": "admin",
            }
        res = TestLogin.sess.request(method="post",url=url,json=data,params=params)
        result = res.json()
        print(result)
        TestLogin.token = result["data"]["token"]
        print(TestLogin.token)



    #查看便民系统订单流水管理
    def test_order_manage(self):
        url = "https://hynq.halixun.com/test/admin/order/page"
        params = {
                "pageNum":1,
                "pageSize:":10,
                "token":TestLogin.token
            }
        res = TestLogin.sess.request(method="get",url=url,params=params)
        result = res.text
        print(result)


    #查看便民系统挂号订单管理
    def test_reserve_order_manage(self):
        url = "https://hynq.halixun.com/test/admin/reserve/page"
        params = {
                "pageNum":1,
                "pageSize:":10,
                "hospitalId":56,
                "token":TestLogin.token
            }
        res = TestLogin.sess.request(method="get",url=url,params=params)
        result = res.text
        print(result)

    #查看便民系统门诊订单管理
    def test_deal_order_manage(self):
        url = "https://hynq.halixun.com/test/admin/order/page"
        params = {
                "pageNum":1,
                "pageSize:":10,
                "hospitalId":56,
                "bizType":2,
                "token":TestLogin.token
            }
        res = TestLogin.sess.request(method="get",url=url,params=params)
        result = res.text
        print(result)


    #查看便民系统住院预交金
    def test_inhospital_money_manage(self):
        url = "https://hynq.halixun.com/test/admin/order/page"
        params = {
                "pageNum":1,
                "pageSize:":10,
                "hospitalId":56,
                "bizType":4,
                "token":TestLogin.token
            }
        res = TestLogin.sess.request(method="get",url=url,params=params)
        result = res.text
        print(result)


    #查看便民系统住院预交金
    def test_merchant(self):
        url = "https://hynq.halixun.com/test/admin/merchant/page"
        data = {
                "pageNum":1,
                "pageSize:":10,
                "orderBy":"%2Bcode",
                "token":TestLogin.token
            }
        params={}
        res = Requestsutil().send_request(method="get",url=url,params=params,data=data)
        result = res.text
        print(result)


