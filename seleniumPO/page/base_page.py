
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:   # 注意名字别写错，否则 其他文件 继承时 会继承或者 继承不到
    base_url = ""
    # 在这里是父类，base_url是设置为空的，但是 子类继承 父类BasePage时，
    # 子类自己是设置如 url="www.baidu.com",是不为空的，所以就从继承的父类这里只是去调用了打开网页的方法 get(self.base_url)

    def __init__(self,driver:WebDriver=None):
        if driver == None:   # 首页判断driver是否为空---即是否是第一次开始使用 driver，为空就创建driver，后面else不为空就直接使用
            option = Options()
            option.debugger_address = "127.0.0.1:9222"
            # 注意 127.0.0.1:9222 需要在本地 开启9222 端口 ----cmd 输入： chrome --remote-debugging-port=9222(端口号可自行设定)
            self.driver = webdriver.Chrome(options=option)

            #   当创建完driver 立即设置隐式等待----万能公式
            self.driver.implicitly_wait(5)  # 踩坑，当没有设置 隐式等待时，报错如图 ---->  有道笔记
        else:
            self.driver = driver
        if self.base_url != "":    # 网页也是一样，第一次url是否为空，因为首页那个网址 只需要打开 一次就可以了，# 而且是在 首页打开页面url，后面就直接复用
            self.driver.get(self.base_url)

    def find(self, locator, value):          # 封装 find, finds 方法，对应 返回的是 find_element  和  find_elements 查找元素方法， 注意传参，也 要意义对应，locator 和 value
        self.driver.find_element(locator, value)
        return self.driver.find_element(locator, value)
    def finds(self,locator, value):
        return self.driver.find_elements(locator, value)

    #  封装 显示等待,
    def wait_for_click(self,timeout,locator):
        WebDriverWait(self.driver,timeout).until(expected_conditions.element_to_be_clickable((locator)))
        # 这里 传入的参数 要 去 源码 看看，  ebDriverWait 需要具体多少个 参数，哪几个 参数 example 那里的例子 看看  ????