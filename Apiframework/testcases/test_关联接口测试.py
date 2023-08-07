__author__ = 'Yourlord'
import requests
import pytest
import re

#部分操作前置，如连接数据库
@pytest.fixture(scope='function')
def conn_database():
    print('连接数据库')
    yield
    print('关闭数据库')

class Testbaidu:


    #前置
    def setup(self):
        print('在用例执行之前的所需执行的步骤')

    #后置
    def teardown(self):
        print('在用例执行之后所需执行的步骤')

    #类变量,作为全局变量
    acces_token=''
    csrf_token=''
    cks=''


#统一请求参数
    def get_session(self):
        session=requests.session()
        return session
    # def test_baidu(self):
    #     url='http:baidu.com'     #接口地址
    #
    #     rep2=requests.post(url=url)
    #     print(rep2.json())
    # if __name__ == '__main__':
    #     pytest.main()

#需要带请求头的接口或者需要cookie的接口如何测试

    #接口A，在此接口返回的接口内容中在下一个接口有需要使用
    @pytest.mark.smoke
    def test_start(self,conn_database):
        url='http://47.107.116.139/phpwind'
        rep=self.get_session().get(url=url)
        print(rep.text)

        Testbaidu.csrf_token = re.search('name="csrf_token"value="(.*?)"',rep.text)[1]
        print(Testbaidu.csrf_token)

    #接口B，需要用到接口A的csrf_token参数
    def test_login(self):
        url='www.baidu.com'
        data={
            'params1':'params1',
            'params2':'Testbaidu.csrf_token',
        }

        headers={
            'Accept':"application/json,text/javascript,/;q=0.01",
            "X-Request-With":"XMLHttpRequest"
        }
        rep2=requests.post(url=url,data=data,cookie=Testbaidu.cks)

        print(rep2.json())

    if __name__ == '__main__':
        pytest.main()