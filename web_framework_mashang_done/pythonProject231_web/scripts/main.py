# '''
# @filename:  /a
# @Author  :  rytest
# @time    :  2023/5/24 14:33
# @Describe:  < >
# '''
# from time import sleep
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# url = "http://47.107.116.139/fangwei/m.php?m=Public&a=login&"
# driver.get(url)
# driver.maximize_window()
#
# driver.add_cookie = {"name": "PHPSESSID",
#                      "value": 'pleqjp11mppqtf1crileq0i1m3'}
#
# driver.add_cookie({"name": "PHPSESSID",
#                    "value": 'e57v354j10d3doqf63udd116v1'})
# # 刷新页面，清楚缓存
# driver.refresh()
# sleep(2)
# driver.refresh()
# sleep(5)
# driver.quit()
# t = (17, 2, '电子行业')
# fields = ['id', 'sort', 'value']
# d = dict(zip(fields, t))
# print(d)
# data = [(3, 1, '汽车行业'), (17, 2, '电子行业'), (19, 4, '测试'), (22, 5, '梵蒂冈的')]
# fields = ['id', 'sort', 'value']
# result = [dict(zip(fields, t)) for t in data]
# print(result)
import logging
import logging.handlers
import time

logger = logging.getLogger()
# 2、设置日志器级别
logger.setLevel(logging.DEBUG)
# 3、创建两个处理器（输出到控制台以及输出到文件）
# 3.1 创建输出到控制台的处理器
sf = logging.StreamHandler()
# 3.2 创建输出到文件的处理器
hf = logging.handlers.TimedRotatingFileHandler("../log/log2.log", when='M', interval=1,
                                               backupCount=3)
# 4、设置级别
sf.setLevel(logging.INFO)
hf.setLevel(logging.INFO)
# 5、创建格式器
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
formatter = logging.Formatter(fmt=fmt)
# 6、添加格式器到处理器当中
sf.setFormatter(formatter)
hf.setFormatter(formatter)
# 7、将处理器添加到日志器
logger.addHandler(sf)
logger.addHandler(hf)
# 8、输出日志信息
while True:
    time.sleep(3)
    logger.info("这是一条信息级别的日志")
    logging.warning("这是一条警告级别的日志")
