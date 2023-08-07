import logging
import jsonpath
from commons.database_util import execute_sql

#获得日志对象
logger =  logging.getLogger(__name__)

#总断言方法
def assert_result(validate,res):
    for key,value in validate.items():
        if key=="codes":
            codes_assert(value,res.status_code)
        elif key=="equals":
            equals_assert(value,res.json())
        elif key=="contains":
            contains_assert(value,res.text)
        elif key=="databases":
            db_assert(value,res.json())
        else:
            logger.error("不支持的断言方式")

#断言日志
def raise_assert_error(msg):
    logger.error(msg)
    logger.info("----------测试用例请求结束----------\n")
    raise AssertionError(msg)

#断言状态码
def codes_assert(yq_code,sj_code):
    if yq_code!=sj_code:
        raise_assert_error("codes断言失败, 预期结果:"+str(yq_code)+",实际结果:"+str(sj_code)+"")

#相等断言
def equals_assert(yq_value,sj_json_value):
    for key,value in yq_value.items():
        list_result = jsonpath.jsonpath(sj_json_value,"$..%s"%key)
        if list_result:
            if value not in list_result:
                raise_assert_error("equals断言失败："+str(key)+" 不等于 "+str(value)+"")
        else:
            raise_assert_error("equals断言失败：返回结果中没有:"+str(key)+"")

#包含断言
def contains_assert(yq_value,sj_text_value):
    if str(yq_value) not in sj_text_value:
        raise_assert_error("contains断言失败:返回结果中不包含"+str(yq_value)+"")

#数据库断言
def db_assert(yq_value,sj_json_value):
    for key,sql in yq_value.items():
        lists = jsonpath.jsonpath(sj_json_value,"$..%s"%key)
        if lists:
            try:
                select_result = execute_sql(sql)
            except:
                raise_assert_error("databases断言失败：SQL查询异常！请检查SQL语句！")
            else:
                #如果select_result的长度为0代表SQL没有查询到值
                if len(select_result)==0:
                    raise_assert_error("databases断言失败：SQL查询没有结果返回！")
                else:
                    if str(lists[0]) not in select_result[0]:
                        raise_assert_error("databases断言失败：预期结果"+str(select_result[0])+"不等于SQL查询的实际结果"+str(lists[0])+"！")
        else:
            raise_assert_error("databases断言失败：返回结果中没有:" + str(key) + "")