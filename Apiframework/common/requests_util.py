__author__ = 'Yourlord'

import json
import requests
#定义一个类变量，在后续使用时直接调用，实际上是定义一个请求方法Requestsutil.send_reques，方便后续大部分测试用例调用时直接调用此方法即可

class Requestsutil:

    #session会话，统一使用一个会话
    session = requests.session()

    #定义一个方法，后续使用是直接调用此方法
    def send_request(self,method,url,params,data,**kwargs):

        method = str(method).lower()   #防止yaml文件中的请求方式写成大写，如POST,此种无法识别

        rep=None #将rep定义成全局变量

        if method =='get':        #get请求需使用params传参
            rep = Requestsutil.session.request(method,url=url,params=params,**kwargs)
        else:
            data =json.dumps(data)
            rep = Requestsutil.session.request(method,url=url,data=data,**kwargs)

        return rep.text           #返回文本格式的内容，兼容性较高



#使用时直接：resp=Requestsutil.send_request(method,url,data)即可
