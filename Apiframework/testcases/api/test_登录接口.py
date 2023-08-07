__author__ = 'Yourlord'
import requests
import pytest

class Testbaoding:

    #保定后台正常登录接口用例
    def test_login(self):
        url='https://jiankangbaoding.cn/test/admin/user/login'
        #键值对
        data={
            "username":"admin",
            "password":"LPh4XyOovMCf",
        }
        rep=requests.post(url=url,json=data)
        #返回json格式的数据
        print(rep.json())
        #增加断言判断用例执行
        assert rep.status_code == 200
        assert rep.json()["message"] == "成功"
        assert rep.json()["code"] == 200



    #保定后台错误密码登录失败接口用例
    def test_wronglogin(self):
        url='https://jiankangbaoding.cn/test/admin/user/login'
        #键值对
        data={
            "username":"admin",
            "password":"wrongpwd",
        }
        rep=requests.post(url=url,json=data)

        #返回json格式的数据
        print(rep.json())

        #增加断言判断用例执行
        assert rep.status_code == 200
        assert rep.json()["message"] == "账号或密码错误"
        assert rep.json()["code"] == 500



if __name__ == '__main__':
    pytest.main()

















