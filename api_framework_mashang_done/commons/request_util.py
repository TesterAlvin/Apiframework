import logging
import re
from io import StringIO
import jsonpath
import requests
import yaml
from commons.assert_util import assert_result
from commons.global_args import load_ini
from commons.yaml_util import write_yaml
from hotloads.debug_talk import DebugTalk

#获得日志对象
logger =  logging.getLogger(__name__)

class RequestUtil:

    #类变量
    sess = requests.session()

    #标准化yaml测试用例
    def standard_yaml_case(self,caseinfo):
        logger.info("----------测试用例请求开始----------")
        #在请求之前调用热加载，通过反射使得yaml能够调用python里面的函数
        yaml_str = yaml.dump(caseinfo)  #把字典转化成字符串
        yaml_str = self.replace_hotload(yaml_str)
        caseinfo = yaml.safe_load(StringIO(yaml_str))  #把字符串转化成字典

        #标准化
        case_keys = caseinfo.keys()
        #如果后者{"title","request","validate"}的超集是set(case_keys)返回True
        if set(case_keys).issuperset({"feature","story","title","request","validate"}):
            request_keys = caseinfo["request"].keys()
            #判断requests目录下必须有method和url
            if set(request_keys).issuperset({"method","url"}):
                # 加入日志：
                logger.info("用例标题：%s" % caseinfo["title"])
                logger.info("请求方式：%s" % caseinfo["request"]["method"])
                logger.info("请求路径：%s" % caseinfo["request"]["url"])
                if set(request_keys).issuperset({"headers"}):
                    logger.info("请求头部：%s" % caseinfo["request"]["headers"])
                #加入公共参数
                if set(request_keys).issuperset({"params"}):
                    params = caseinfo["request"]["params"]
                    params.update(load_ini())
                    caseinfo["request"]["params"] = params
                else:
                    params = {}
                    params.update(load_ini())
                    caseinfo["request"]["params"] = params
                # 处理files，同时存在？
                for key,value in caseinfo["request"].items():
                    if key == "params":
                        logger.info("请求params参数：%s" % caseinfo["request"]["params"])
                    elif key == "data":
                        logger.info("请求data参数：%s" % caseinfo["request"]["data"])
                    elif key == "json":
                        logger.info("请求json参数：%s" % caseinfo["request"]["json"])
                    if key == "files":
                        logger.info("用例files参数：%s" % caseinfo["request"]["files"])
                        for file_key, file_value in value.items():
                            value[file_key] = open(file_value, "rb")
                #发送请求
                res = self.send_all_request(**caseinfo["request"])
                logger.info("预期结果：%s" % caseinfo["validate"])
                logger.info("实际结果：%s" % res.text)
                #提取中间变量
                self.extract_yaml_value(caseinfo,res)
                #断言封装
                if caseinfo['validate']:
                    assert_result(caseinfo['validate'],res)
                #接口测试通过
                logger.info("接口测试通过!")
                logger.info("----------测试用例请求结束----------\n")
            else:
                logger.error("YAML中的request目录下必须包含method,url")
                logger.info("----------测试用例请求结束----------\n")
        else:
            logger.error("YAML一级目录必须包含feature,story,title,request,validate")
            logger.info("----------测试用例请求结束----------\n")

    #封装的统一发送请求的方法
    def send_all_request(self,**kwargs):
        #统一请求
        res = RequestUtil.sess.request(**kwargs)
        print(res.text)
        return res

    #通过extract提取中间变量保存到extract.yaml里面
    def extract_yaml_value(self,caseinfo,res):
        if "extract" in caseinfo.keys():
           for key,value in caseinfo["extract"].items():
               #正则提取
               if "(.*?)" in value or "(.+?)" in value:
                    zz_value = re.findall(value,res.text)
                    if len(zz_value)==0:
                        logger.error("正则没有提取到任何值！")
                    else:
                        if len(zz_value)==1:
                            #只提取到一个值
                            data = {key: zz_value[0]}
                            write_yaml(data)
                        else:
                            #提取到多个值
                            data = {key: zz_value}
                            write_yaml(data)
               else:  #jsonpath提取
                   js_value = jsonpath.jsonpath(res.json(),value)
                   if js_value:
                       if len(js_value)==1:
                           # 只提取到一个值
                           data = {key: js_value[0]}
                           write_yaml(data)
                       else:
                           # 提取到多个值
                           data = {key: js_value}
                           write_yaml(data)

    #热加载httprunner
    def replace_hotload(self,yaml_str):
        regexp = "\\${(.*?)\\((.*?)\\)}"
        fun_list = re.findall(regexp,yaml_str)
        for f in fun_list:
            if f[1]=="":  #没有参数
                #反射
                new_value = getattr(DebugTalk(),f[0])()
            else:  #有参数
                new_value = getattr(DebugTalk(), f[0])(*f[1].split(","))
            oldstr = "${"+f[0]+"("+f[1]+")}" #拼接旧值
            yaml_str = yaml_str.replace(oldstr,str(new_value))
        return yaml_str