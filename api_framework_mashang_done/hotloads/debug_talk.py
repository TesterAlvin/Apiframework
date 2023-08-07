import base64
import hashlib
import os
import random
import re
import time
from io import StringIO
import rsa
import yaml

class DebugTalk:

    # 读取config.yaml的数据
    def read_config(self,key):
        with open(os.getcwd() + "/config.yaml", encoding="utf-8", mode="r") as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[key]

    # 读取yaml的数据
    def read_yaml(self,key):
        with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="r") as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[key]

    # 读取yaml的数据
    def read_yaml_of_index(self, key,index):
        with open(os.getcwd() + "/extract.yaml", encoding="utf-8", mode="r") as f:
            value = yaml.load(f, yaml.FullLoader)
            return value[key][int(index)]

    #随机数
    def get_time(self,length):
        return str(int(time.time()))[:length]

    #md5加密
    def md5_encode(self,args):
        #把变量转化成utf-8的编码格式
        args = str(args).encode("utf-8")
        #md5加密
        md5_value = hashlib.md5(args).hexdigest()
        return md5_value

    # base64加密
    def base64_encode(self, args):
        # 把变量转化成utf-8的编码格式
        args = str(args).encode("utf-8")
        # md5加密
        base64_value = base64.b64encode(args).decode(encoding="utf-8")
        return base64_value

    #生成RSA的公钥和私钥（做测试一般是直接拿到公钥和私钥）
    # def create_key(self):
    #     (public_key,private_key)=rsa.newkeys(1024)
    #     with open("./public.pem","w+") as f:
    #         f.write(public_key.save_pkcs1().decode())
    #     with open("./private.pem","w+") as f:
    #         f.write(private_key.save_pkcs1().decode())

    #rsa加密
    def ras_encode(self,args):
        with open("./hotloads/public.pem") as f:
            pubkey =rsa.PublicKey.load_pkcs1(f.read().encode())
        # 把变量转化成utf-8的编码格式
        args = str(args).encode("utf-8")
        #把字符串加密成byte类型
        byte_value = rsa.encrypt(args,pubkey)
        #把字节转化成字符串格式
        rsa_value = base64.b64encode(byte_value).decode("utf-8")
        return rsa_value

    # 数据驱动的sign签名
    def ddt_sign(self, yaml_path,index):
        all_dict_data = {}
        # 第一步
        with open(os.getcwd() + "/" + yaml_path, encoding="utf-8") as f:
            yaml_value = yaml.safe_load(f)

            # 数据驱动
            new_caseinfo = self.ddts(*yaml_value)
            case = new_caseinfo[int(index)]

            #签名
            case_keys = case.keys()
            if "request" in case_keys:
                request_value = case["request"]
                # 把url的?之后的值转化成字典
                if "url" in request_value.keys():
                    url = request_value["url"]
                    url = url[url.index("?") + 1:]
                    url_list = url.split("&")
                    for u in url_list:
                        all_dict_data[u[0:u.index("=")]] = u[u.index("=") + 1:]
                print(all_dict_data)
                # 得到params和data的参数
                for key, value in request_value.items():
                    if key in ["data", "params"]:
                        for k, v in value.items():
                            all_dict_data[k] = v
                print(all_dict_data)
                # dict中的key根据asscii码排序
                all_dict_data = self.dict_asccii_sort(all_dict_data)
                # 热加载
                yaml_str = yaml.dump(all_dict_data)  # 把字典转化成字符串
                yaml_str = self.replace_hotload(yaml_str)
                all_dict_data = yaml.safe_load(StringIO(yaml_str))  # 把字符串转化成字典
                print(all_dict_data)

        # 第二步
        all_str = ""
        for key, value in all_dict_data.items():
            all_str = all_str + str(key) + "=" + str(value) + "&"
        all_str = all_str[:-1]
        print(all_str)
        # 第三-五步
        appid = "admin"
        appsecret = "123"
        nonce = str(random.randint(1000000000, 9999999999))
        timestamp = str(int(time.time()))
        all_str = "appid=" + appid + "&" + "appsecret=" + appsecret + "&" + all_str + "&" + "nonce=" + nonce + "&""timestamp=" + timestamp + ""
        print(all_str)
        # 第六步
        sign = self.md5_encode(all_str).upper()
        print(sign)
        return sign

    # 流程用例的sign签名
    def flow_sign(self, yaml_path, index):
        all_dict_data = {}
        # 第一步
        with open(os.getcwd() + "/" + yaml_path, encoding="utf-8") as f:
            yaml_value = yaml.safe_load(f)

            # 数据驱动
            case = yaml_value[int(index)]

            # 签名
            case_keys = case.keys()
            if "request" in case_keys:
                request_value = case["request"]
                # 把url的?之后的值转化成字典
                if "url" in request_value.keys():
                    url = request_value["url"]
                    url = url[url.index("?") + 1:]
                    url_list = url.split("&")
                    for u in url_list:
                        all_dict_data[u[0:u.index("=")]] = u[u.index("=") + 1:]
                print(all_dict_data)
                # 得到params和data的参数
                for key, value in request_value.items():
                    if key in ["data", "params"]:
                        for k, v in value.items():
                            all_dict_data[k] = v
                print(all_dict_data)
                # dict中的key根据asscii码排序
                all_dict_data = self.dict_asccii_sort(all_dict_data)
                # 热加载
                yaml_str = yaml.dump(all_dict_data)  # 把字典转化成字符串
                yaml_str = self.replace_hotload(yaml_str)
                all_dict_data = yaml.safe_load(StringIO(yaml_str))  # 把字符串转化成字典
                print(all_dict_data)

        # 第二步
        all_str = ""
        for key, value in all_dict_data.items():
            all_str = all_str + str(key) + "=" + str(value) + "&"
        all_str = all_str[:-1]
        print(all_str)
        # 第三-五步
        # appid = "admin"
        # appsecret = "123"
        # nonce = str(random.randint(1000000000, 9999999999))
        # timestamp = str(int(time.time()))
        # all_str = "appid=" + appid + "&" + "appsecret=" + appsecret + "&" + all_str + "&" + "nonce=" + nonce + "&""timestamp=" + timestamp + ""
        # print(all_str)
        # 第六步
        sign = self.md5_encode(all_str).upper()
        print(sign)
        return sign

    # #普通sign签名
    # def signs(self,yaml_path):
    #     all_dict_data = {}
    #     #第一步
    #     with open(os.getcwd()+"/"+yaml_path,encoding="utf-8") as f:
    #         yaml_value = yaml.safe_load(f)
    #         for case in yaml_value:
    #             case_keys = case.keys()
    #             if "request" in case_keys:
    #                 request_value = case["request"]
    #                 # 把url的?之后的值转化成字典
    #                 if "url" in request_value.keys():
    #                     url = request_value["url"]
    #                     url = url[url.index("?")+1:]
    #                     url_list = url.split("&")
    #                     for u in url_list:
    #                         all_dict_data[u[0:u.index("=")]] = u[u.index("=")+1:]
    #                 print(all_dict_data)
    #                 #得到params和data的参数
    #                 for key,value in request_value.items():
    #                     if key in ["data","params"]:
    #                         for k,v in value.items():
    #                             all_dict_data[k] = v
    #                 print(all_dict_data)
    #                 #dict中的key根据asscii码排序
    #                 all_dict_data = self.dict_asccii_sort(all_dict_data)
    #                 #热加载
    #                 yaml_str = yaml.dump(all_dict_data)  # 把字典转化成字符串
    #                 yaml_str = self.replace_hotload(yaml_str)
    #                 all_dict_data = yaml.safe_load(StringIO(yaml_str))  # 把字符串转化成字典
    #                 print(all_dict_data)
    #
    #     # 第二步
    #     all_str = ""
    #     for key,value in all_dict_data.items():
    #         all_str = all_str+str(key)+"="+str(value)+"&"
    #     all_str = all_str[:-1]
    #     print(all_str)
    #     # 第三-五步
    #     appid = "admin"
    #     appsecret = "123"
    #     nonce = str(random.randint(1000000000,9999999999))
    #     timestamp = str(int(time.time()))
    #     all_str = "appid="+appid+"&"+"appsecret="+appsecret+"&"+all_str+"&"+"nonce="+nonce+"&""timestamp="+timestamp+""
    #     print(all_str)
    #     #第六步
    #     flow_sign.yaml = self.md5_encode(all_str).upper()
    #     print(flow_sign.yaml)
    #     return flow_sign.yaml

    # 把字典安装key的Asccii码升序排序
    def dict_asccii_sort(self, args_dict):
        dict_key = dict(args_dict).keys()
        l = list(dict_key)
        l.sort()
        new_dict = {}
        for key in l:
            new_dict[key] = args_dict[key]
        return new_dict

    # 热加载httprunner
    def replace_hotload(self, yaml_str):
        regexp = "\\${(.*?)\\((.*?)\\)}"
        fun_list = re.findall(regexp, yaml_str)
        for f in fun_list:
            if f[1] == "":  # 没有参数
                # 反射
                new_value = getattr(DebugTalk(), f[0])()
            else:  # 有参数
                new_value = getattr(DebugTalk(), f[0])(*f[1].split(","))
            oldstr = "${" + f[0] + "(" + f[1] + ")}"  # 拼接旧值
            yaml_str = yaml_str.replace(oldstr, str(new_value))
        return yaml_str

    # 解析数据驱动parametrize
    def ddts(self,caseinfo):
        # 把字典转化成字符串格式
        str_caseinfo = yaml.dump(caseinfo)  # 把字典转化成字符串
        case_list = caseinfo["parametrize"]
        # 初步判断数据的长度是否异常
        length_flag = True
        name_length = len(caseinfo["parametrize"][0])
        for p in case_list:
            if len(p) != name_length:
                length_flag = False
        # 长度没有问题
        new_caseinfo = []
        if length_flag:
            for x in range(1, len(case_list)):  # 行
                raw_caseinfo = str_caseinfo
                for y in range(0, name_length):  # 列
                    # 解决数字字符串变成了数字类型的问题
                    if isinstance(case_list[x][y], str):
                        case_list[x][y] = "'" + str(case_list[x][y]) + "'"
                    raw_caseinfo = raw_caseinfo.replace("$ddt{" + case_list[0][y] + "}", str(case_list[x][y]))
                new_caseinfo.append(yaml.safe_load(StringIO(raw_caseinfo)))
        return new_caseinfo

