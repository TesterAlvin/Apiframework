from selenium.webdriver import Chrome, Firefox, Ie, Safari


def get_webdriver(name: str = 'chrome'):
    # 根据名字，启动特定的浏览器
    # 将所有的name转化为小写
    name = name.lower()
    # 将所有的name中的空格去掉
    name = name.replace(" ", "")
    match name:
        case "chrome":
            return Chrome()
        case "firefox":
            return Firefox()
        case "ie":
            return Ie()
        case "safari":
            return Safari()
