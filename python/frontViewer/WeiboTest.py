#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

class WeiboTest:
    def __init__(self, webdriver):
        self.driver = webdriver
        self.waitAfterOperation = 2
        self.waitAfterBigOperation = 5
        
    def openWriteNewStatus(self):
        mybtn = self.driver.find_element_by_class_name('iconf_navbar_compose')
        mybtn.click()
        time.sleep(self.waitAfterBigOperation)
        
    def typeWeibo(self, content):
        el = self.driver.find_element_by_id('txt-publisher')
        #el.send_keys(Keys.CONTROL, 'v') #Parse.
        el.send_keys(content)
        mybtn = self.driver.find_element_by_css_selector('.module-topbar .fr')
        mybtn.click()
        time.sleep(self.waitAfterBigOperation)
        
    def checkAtlist(self):
        #switch from frontpage to at list.
        self.driver.get('http://m.weibo.cn/msg/atme?subtype=allWB')
        contentlist = self.driver.find_elements_by_class_name('default-content')
        timelist = self.driver.find_elements_by_class_name('time')
        if(not len(timelist) == len(contentlist)):
            print ("not equal...")
            return False
        for i in range(0, contentlist):
            if('@一键吃书井上葵' in contentlist[i]):
                print ("we got a call at " + timelist[i])
        
        