# 重新考虑获取一个驱动去执行新增贷款页面，不需要考虑直接使用已登录的驱动进行后面的逻辑操作
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from scripts.login import driver

# print(driver.title)

# //*[@id="navs"]/ul/li[2]/a

# 点击贷款管理
frame = driver.find_element(By.XPATH, '/html/frameset/frame[1]')
# 切入子页面(有始有终，一旦进去就要记得退出)
driver.switch_to.frame(frame)
driver.find_element(By.XPATH, '//*[@id="navs"]/ul/li[2]/a').click()
# 退出子页面
driver.switch_to.default_content()
# 此处强制等待，为了看到操作过程
time.sleep(3)

# 点击全部贷款
frame = driver.find_element(By.XPATH, '//*[@id="menu-frame"]')
# 切入子页面(有始有终，一旦进去就要记得退出)
driver.switch_to.frame(frame)
driver.find_element(By.XPATH, '/html/body/dl[1]/dd[1]/a').click()
# 退出子页面
driver.switch_to.default_content()
# 此处强制等待，为了看到操作过程
time.sleep(3)

# 点击新增贷款
frame = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
# 切入子页面(有始有终，一旦进去就要记得退出)
driver.switch_to.frame(frame)
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/input[1]').click()
# 退出子页面
driver.switch_to.default_content()
# 此处强制等待，为了看到操作过程
time.sleep(3)

# 元素的操作
# 颜色
frame = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
# 切入子页面(有始有终，一旦进去就要记得退出)
driver.switch_to.frame(frame)
driver.find_element(By.XPATH, '//*[@id="colorpickerField"]').send_keys('f00')
# 贷款编号
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[3]/td[2]/input').clear()
time.sleep(1)  # 此处强制等待，为了看到操作过程
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[3]/td[2]/input').send_keys('DK666')
# 贷款名称
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input').send_keys('需要融资上市100亿')
time.sleep(1)
# 简短名称
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input').send_keys('100E')
# 会员名称
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]').send_keys('beifan')
# 选中具体会员名称
time.sleep(3)
driver.find_element(By.XPATH, '//strong[text()="beifan"]').click()
# 选中城市信息
driver.find_element(By.XPATH, '//*[@id="citys_box"]/div[1]/div[2]/input[3]').click()

# 分类:
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select')
select1 = Select(sl1)
# 定位下拉框元素有3中方式：通过下标（从0开始），通过值定位（value），通过文本内容定位
# 通过下标（从0开始）
select1.select_by_index(2)
time.sleep(2)
# 担保机构
sl2 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[9]/td[2]/select')
select2 = Select(sl2)
# 定位下拉框元素有3中方式：通过下标（从0开始），通过值定位（value），通过文本内容定位
# 通过值定位（value）
select2.select_by_value('2181')
time.sleep(2)
# 担保范围
sl3 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[10]/td[2]/select')
select3 = Select(sl3)
# 定位下拉框元素有3中方式：通过下标（从0开始），通过值定位（value），通过文本内容定位
# 通过下标（从0开始）
select3.select_by_visible_text('无')
# 借款用途
sl3 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select')
select3 = Select(sl3)
# 定位下拉框元素有3中方式：通过下标（从0开始），通过值定位（value），通过文本内容定位
# 通过下标（从0开始）
select3.select_by_visible_text('婚礼筹备')

# 文件上传
# 点击图片上传
driver.find_element(By.XPATH, '/html/body/div[2]'
                              '/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button').click()
# 本地上传：(当元素交互比较复杂时，尽量加等待时间)
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[2]/div/div[1]/ul/li[2]').click()

# 预览文件上传：
driver.find_element(By.XPATH, '//input[@type="file"]').send_keys(r'D:\pythonProject231_web\verify.png')
# 点击确定
driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[3]/span[1]/input').click()

# ...
# 筹标中
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]').click()
time.sleep(2)
# 开始时间的选择
el1 = driver.find_element(By.XPATH, '//*[@id="start_time"]')
# 通过js脚本代码(固定格式)进行强制输入,arguments.value固定值传递实参值
driver.execute_script('arguments.value="2023-05-14 21:56:58"', el1)

input("调试触发，需要结束：")
# 关闭浏览器驱动
driver.quit()
