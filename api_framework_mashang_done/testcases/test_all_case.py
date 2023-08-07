from pathlib import Path
import allure
import pytest
import yaml
from commons.ddt_util import read_testcase
from commons.request_util import RequestUtil

#当前路径
cuurent_path = Path(__file__).parent
#找到所有的代表测试用例的yaml文件
yaml_case_list = cuurent_path.glob("**/*.yaml")

@allure.epic("项目名称：码尚教育B2C商城接口自动化测试")
class TestAllApi:
    pass

#创建用例的方法
def create_testcase(yaml_path):
    #读取yaml。读取后是一个list
    with open(yaml_path,mode="r",encoding="utf-8") as f:
        caseinfo = yaml.load(f,yaml.FullLoader)


    # 用例
    @allure.feature(caseinfo[0]["feature"])
    @allure.story(caseinfo[0]["story"])
    #@allure.title("{caseinfo[title]}")
    @pytest.mark.parametrize("caseinfo",read_testcase(yaml_path))
    def test_func(self,caseinfo):
        if isinstance(caseinfo,list):  #流程用例
            for case in caseinfo:
                allure.dynamic.title(case["title"])
                RequestUtil().standard_yaml_case(case)
        else:  #单接口用例
            allure.dynamic.title(caseinfo["title"])
            RequestUtil().standard_yaml_case(caseinfo)

    #返回用例
    return test_func

# 循环所有的yaml用例的文件名
for yaml_path in yaml_case_list:
    #yaml的名字
    yaml_name = yaml_path.name[:-5]
    #表示在类TestAllApi中增加一个名字为yaml_name测试用例
    setattr(TestAllApi, f"test_{yaml_name}", create_testcase(yaml_path))