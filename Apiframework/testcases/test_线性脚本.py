__author__ = 'Yourlord'
import requests
import pytest

class Testxianxingrequest:

    def test_get_token(self):

      #查询token使用情况  get方法
        url='https://api.ip138.com/status/'

        #键值对
        params={
            'token':'6a9ebb3df93ae67655e0c22d98d99305'
        }
        rep=requests.get(url=url,params=params)

#返回字符串格式的数据
        print(rep.text)

if __name__ == '__main__':
    pytest.main()


    def test_upload_file(self):
        url='https:test.com'     #接口地址

        #上传文件代码格式，以二进制文件打开上传，需先打开后上传
        data={
            'params':open(r'E:\test.text','rb')
        }
        rep2=requests.post(url=url,data=data)
        print(rep2.json())


        #返回字节格式的数据
        # print(rep.content)
        #
        # #返回字典格式的数据
        # print(rep.json())
        #
        # #返回状态码
        # print(rep.status_code)
        #
        # #返回状态信息
        # print(rep.reason)
        #
        # #返回cookie信息
        # print(rep.cookies)
        #
        # #返回编码格式
        # print(rep.encoding)
        #
        # #返回响应头信息
        # print(rep.headers)







#发送get请求实战操作     接口存在异常  接口返回无效手机号
# url='http://api.ip138.com/mobile/'
# params={
#     'mobile string ':'13209760000',
#     'token':'6a9ebb3df93ae67655e0c22d98d99305'
# }
#
# #传参说明
# # token	string	是	用户授权
# #mobile strtin  是  手机号码
# rsp=requests.get(url=url,params=params)
# print(rsp.text)








