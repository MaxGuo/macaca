#coding:utf-8

import unittest
import os
import time
from macaca import WebDriver
from retrying import retry

desired_caps = {
    'platformName': 'iOS',
    'deviceName': 'iPhone 6s',
    'udid':'aa7ec70ec3683c044ad96d27e0c97e76f3386e54',
    #'app': 'http://192.168.3.53/MpmMerchant.zip',
    'bundleId':'com.imicrothink.MeiPingMi',
}


server_url = {
    'hostname': 'localhost',
    'port': 3456
}

def switch_to_webview(driver):
    contexts = driver.contexts
    driver.context = contexts[-1]
    return driver

def switch_to_native(driver):
    contexts = driver.contexts
    driver.context = contexts[0]
    return driver

class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.initDriver()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    @retry
    def initDriver(cls):
        print("Retry connecting server...")
        cls.driver.init()

        time.sleep(5)

    def test_01_login(self): #密码登录
        self.driver \
            .element_by_name('我的') \
            .click()
        #点击"我的"

        self.driver \
            .element_by_name('密码登录') \
            .click()
        # 点击"密码登录"


        self.driver \
            .element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]') \
            .send_keys('13805728638')   \
        #输入手机号码

        self.driver \
            .element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeSecureTextField[1]') \
            .send_keys('gjm123') \
        #输入密码

        time.sleep(2)


        self.driver \
            .element_by_name('登   录') \
            .click()
        #点击登录

    time.sleep(5)

    def test_02_scroll_tableview(self):   #切换tab
        self.driver              \
            .element_by_name('购物车') \
            .click()

        self.driver             \
            .element_by_name('分类') \
            .click()

        self.driver \
            .element_by_name('首页') \
            .click()

    #def test_03_gesture(self):
        #self.driver \
            #.touch('drag', {
            #  'fromX': 200,
            #  'fromY': 400,
            #  'toX': 200,
            #  'toY': 100,
            #  'duration': 2
            #})

        #time.sleep(1)

        #self.driver \
            #.touch('drag', {
            #  'fromX': 100,
            #  'fromY': 100,
            #  'toX': 100,
            #  'toY': 400,
            #  'duration': 2
            #})

        #time.sleep(1)

        #self.driver \
           # .element_by_name('首页') \
           # .click()

        #self.driver \
           # .touch('tap', {
           #   'x': 100,
            #  'y': 100
           # })

        #time.sleep(1)

        #self.driver \
           # .touch('press', {
           #   'x': 100,
           #   'y': 100,
           #   'duration': 1
           # })

        #time.sleep(1)

        #self.driver \
           # .element_by_id('') \
           # .touch('pinch', {
           #   'scale': 2,
           #   'velocity': 1
           # })

        #time.sleep(1)

        #self.driver \
            #.touch('drag', {
           #   'fromX': 100,
           #   'fromY': 100,
           #   'toX': 100,
           #   'toY': 600,
           #   'steps': 100
           # })

    time.sleep(5)

    def test_04_my_oraders(self): #查看订单

        self.driver \
            .element_by_name('我的') \
            .click()
        # 点击"我的"

        time.sleep(3)

        self.driver \
            .element_by_name('查看全部订单') \
            .click()
        # 点击"查看全部订单"

        self.driver \
         .touch('tap', {
           'x': 0,
          'y': 100
         })

        self.driver \
            .touch('tap', {
            'x': 0,
            'y': 100
        })

        self.driver \
            .element_by_name('bt back') \
            .click()
        # 点击"返回"

        time.sleep(1)

        self.driver \
            .element_by_name('待付款') \
            .click()
        # 点击"待付款"
        time.sleep(3)

        self.driver \
            .touch('tap', {
            'x': 0,
            'y': 100
        })

        self.driver \
            .touch('tap', {
            'x': 100,
            'y': 100
        })

        self.driver \
            .element_by_name('bt back') \
            .click()
        # 点击"返回"

        time.sleep(1)

        self.driver \
            .element_by_name('待发货') \
            .click()
        # 点击"待发货"
        time.sleep(3)

        self.driver \
            .touch('tap', {
            'x': 0,
            'y': 100
        })

        self.driver \
            .touch('tap', {
            'x': 0,
            'y': 100
        })

        self.driver \
            .element_by_name('bt back') \
            .click()
        # 点击"返回"

        time.sleep(1)

        self.driver \
            .element_by_name('待收货') \
            .click()
        # 点击"待收货"
        time.sleep(3)

        self.driver \
            .touch('tap', {
            'x': 0,
            'y': 100
        })

        self.driver \
            .touch('tap', {
            'x': 0,
            'y': 100
        })

        self.driver \
            .element_by_name('bt back') \
            .click()
        # 点击"返回"

        time.sleep(1)

        self.driver \
            .element_by_name('退换货') \
            .click()
        # 点击"退换货"
        time.sleep(3)

        self.driver \
            .touch('tap', {
            'x': 0,
            'y': 100
        })

        self.driver \
            .touch('tap', {
            'x': 0,
            'y': 100
        })

        self.driver \
            .element_by_name('bt back') \
            .click()
        # 点击"返回"

    time.sleep(5)


    def test_05_my_setting(self):#设置
        self.driver \
            .element_by_name('设置') \
            .click()
        # 点击"设置"

        self.driver \
            .element_by_name('个人资料') \
            .click()
        # 查看个人资料
        time.sleep(3)

        #以下为修改头像

        self.driver \
            .element_by_name('头像') \
            .click()
        # 点击"头像"
        time.sleep(3)

        self.driver \
            .element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeImage[1]') \
            .click()
        #点击图片
        time.sleep(3)

        self.driver \
            .element_by_name('相机') \
            .click()
        # 选择相机
        time.sleep(3)

        self.driver \
            .element_by_name('PhotoCapture') \
            .click()
        # 点击拍照按钮
        time.sleep(3)

        self.driver \
            .element_by_name('重拍') \
            .click()
        # 点击重拍
        time.sleep(3)

        self.driver \
            .element_by_name('PhotoCapture') \
            .click()
        # 点击拍照按钮
        time.sleep(3)

        self.driver \
            .element_by_name('使用照片') \
            .click()
        # 点击使用照片
        time.sleep(3)

        self.driver \
            .element_by_name('bt back') \
            .click()
        # 点击"返回"










        time.sleep(1)

        self.driver \
            .element_by_name('bt back') \
            .click()
        # 点击"返回"

        time.sleep(5)





        #switch_to_native(self.driver) \
            #.element_by_name('Baidu') \
            #.touch('tap')

        #time.sleep(3)
        #self.driver.save_screenshot("./baidu.png")

        #switch_to_webview(self.driver) \
            #.element_by_id('index-kw') \
            #.send_keys('macaca') \
            #.element_by_id('index-bn') \
            #.touch('tap')

    def test_06_logout(self):#退出登录
        self.driver \
            .element_by_name('设置') \
            .click()
        # 点击"设置"

        time.sleep(2)

        self.driver \
            .element_by_name('退出当前账号') \
            .click()
        # 点击"退出"
        time.sleep(2)

        self.driver \
            .element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]') \
            .click()
        # 点击"取消"
        time.sleep(2)

        self.driver \
            .element_by_name('退出当前账号') \
            .click()
        # 点击"退出"
        time.sleep(2)

        self.driver \
            .element_by_xpath('//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeAlert[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]') \
            .click()
        # 点击"确定"
        time.sleep(2)





if __name__ == '__main__':
    unittest.main()
