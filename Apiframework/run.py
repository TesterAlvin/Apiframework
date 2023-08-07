__author__ = 'Yourlord'
#执行文件，一次性执行所有用例

#导入对应的模块os、pytest包
import pytest
import os
import time


#主函数
if __name__ == '__main__':
    pytest.main()

    #增加等待时间，防止json文件生成延迟
    time.sleep(2)

    #使用os文件系统命令，通过生成的临时json文件输出allure测试报告至report目录下，再通过使用浏览器（Chrome、Firefox）
    #打开index.html文件查看allure测试报告内容
    os.system('allure generate ./temp -o reports --clean')


    #注：--clean  清除原有测试报告，才能重新写入测试报告

