import json
import logging
from io import StringIO
import yaml
#获得日志对象
logger =  logging.getLogger(__name__)

#读取测试用例的方法
def read_testcase(yaml_path):
    with open(yaml_path,encoding="utf-8",mode="r") as f:
        caseinfo = yaml.load(f,yaml.FullLoader)
        if len(caseinfo)>=2:   #通过复制yaml数据的方式实现数据驱动
            return [caseinfo]  #[[{},{}]]
        else:   #通过parametrize标签实现的数据驱动
            if "parametrize" in dict(*caseinfo).keys():
                new_caseinfo = ddts(*caseinfo)
                print(new_caseinfo)
                return new_caseinfo
            else:
                return caseinfo

#解析数据驱动parametrize，[{}] 改成 [{},{}]
def ddts(caseinfo):
    #把字典转化成字符串格式
    str_caseinfo = yaml.dump(caseinfo)  # 把字典转化成字符串
    case_list = caseinfo["parametrize"]
    #初步判断数据的长度是否异常
    length_flag = True
    name_length = len(caseinfo["parametrize"][0])
    for p in case_list:
        if len(p)!=name_length:
            length_flag = False
            logger.error("此数据长度有误：%s"%p)
    #长度没有问题
    new_caseinfo=[]
    if length_flag:
        for x in range(1,len(case_list)):   #行
            raw_caseinfo=str_caseinfo
            for y in range(0,name_length):  #列
                # 解决数字字符串变成了数字类型的问题
                if isinstance(case_list[x][y],str):
                    case_list[x][y] = "'"+str(case_list[x][y])+"'"
                raw_caseinfo = raw_caseinfo.replace("$ddt{" + case_list[0][y] + "}",str(case_list[x][y]))
            new_caseinfo.append(yaml.safe_load(StringIO(raw_caseinfo)))
    return new_caseinfo