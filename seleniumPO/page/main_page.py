

#  企业微信 主页
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from Web_autotest_jenkins_demo.seleniumPO.page.add_member import AddMemberPage
from Web_autotest_jenkins_demo.seleniumPO.page.base_page import BasePage


class MainPage(BasePage):
    #    可以将这一块 删掉， 已经被 封装到 BasePage,并 在这里 继承#
    base_url = "https://work.weixin.qq.com/wework_admin/frame"
    # 首页一定要写上  url， 不写的话，会默认去 前面复用浏览器时，任何一个停留的页面进行操作，不一定是首页，所以会出现找不到元素，报错
    def goto_add_member(self):

        '''
        添加成员
        :return:
        '''

        # click add member
        self.find(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()  # BasePage 已经封装了 find 方法，将下面进行改造
        # self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMemberPage(self.driver)