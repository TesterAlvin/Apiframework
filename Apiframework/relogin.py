import logging
import logging.config
import os

#日志文件输出
'''logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%a,%d,%b,%Y,%H:%S',
                    filename="D:/Log/loging.log)")
logger = logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")'''

'''logging.basicConfig(filename="./loging.log",filemode='w',level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s -%(lineno)s - %(message)s')
logging.debug('这个是一个调试信息')
logging.info('这是一个info调试')
logging.error('这个是一个严重的bug')'''

''''#这个创建一个记录笔
logger =logging.getLogger('cn.cccb.wanduzi')
#设置记录笔默认打印级别,级别取最高级别
logger.setLevel(logging.DEBUG)

#控制台输出
consoleHandler = logging.StreamHandler()
#设置控制台输出级别
consoleHandler.setLevel(logging.INFO)
#设置文本输出
fileHandler = logging.FileHandler(filename='loging.log')
#文本输出的级别
fileHandler.setFormatter(logging.INFO)

#设置输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s    - %(filename)s -%(lineno)s - %(message)s')
#设置控制台输出格式
consoleHandler.setFormatter(formatter)
#设置文本输出格式
fileHandler.setFormatter(formatter)

#把输入个设置添加到logger
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

#定义一个过滤器(过滤只打印cn.cccb令名的
fit = logging.Filter('cn.cccb')
logger.addFilter(fit)'''
def log_fire():
    #print(os.getcwd())
    #logfire = str(os.getcwd()) + '\logging.conf'
    #logfire.replace('\\','/')
    #print(logfire)

    #print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

    logging.config.fileConfig('./logging.conf')
    logger = logging.getLogger('root')

    #logger.debug('这是一个bug')
    return logger

#logfire = str(os.path.dirname(__file__)) + '\logging.conf'
def log_fire1():
    #print(os.getcwd())
    #print(os.path.dirname(__file__))
    logfire = str(os.path.dirname(__file__)) + '\logging.conf'
    #print(logfire)
    logfire.replace('\\','/')
    #print(logfire)
    #print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    logging.config.fileConfig(logfire)
    logger = logging.getLogger('root')
    #logger.debug('这是一个bug')
    return logger

def log_fire2():
    #print(os.getcwd())
    logfire1 = str(os.path.abspath(os.path.join(os.getcwd(), "../.."))) + '\logging.conf'
    logfire1.replace('\\','/')
    #print(logfire)
    #print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    print(logfire1)
    logging.config.fileConfig(logfire1)
    logger = logging.getLogger('root')
    #logger.debug('这是一个bug')
    return logger
def log_fire4():
    logfire = r'E:/XWtest/logging.conf'
    logging.config.fileConfig(logfire)
    logger = logging.getLogger('root')
    return logger
def log_fire5():
    logfire = str(os.path.dirname(__file__))+'\logging.conf'
    logfire = logfire.replace('\\','/')
    logging.config.fileConfig(logfire)
    logger = logging.getLogger('root')
    return logger





