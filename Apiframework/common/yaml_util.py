__author__ = 'Yourlord'
import os
import yaml

class YamlUtil:
    #读取yaml文件
    def read_extract_yaml(self,key):
        with open(os.getcwd()+"/extract.yaml",mode='r',encoding='utf-8')as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]


    #写入yaml文件
    def write_extract_yaml(self,key):
        with open(os.getcwd()+"/extract.yaml",mode='w',encoding='utf-8')as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]


    #清除yaml文件
    def clear_extract_yaml(self):
        with open(os.getcwd()+"/extract.yaml",mode='w',encoding='utf-8')as f:
            f.truncate()


    #读取测试用例的接口文件
    def read_testcase_yaml(self,yaml_name):
        with open(os.getcwd()+"/testcase"+yaml_name,mode='r',encoding='utf-8')as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value
