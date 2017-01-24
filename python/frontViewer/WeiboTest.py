#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import CoreHandler

class WeiboTest:
    def __init__(self, webdriver):
        self.driver = webdriver
        self.ch = CoreHandler.CoreHandler('一键吃书井上葵')
        self.waitAfterOperation = 2
        self.waitAfterBigOperation = 5
        
    def openWriteNewStatus(self):
        self.driver.get('http://m.weibo.cn/mblog')
        
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
        authorlist = self.driver.find_elements_by_css_selector('a.item-main')
        if (not len(timelist) == len(contentlist)):
            print ("not equal...")
            return False
        for i in range(0, len(contentlist)):
            mycontent = contentlist[i].text
            author = authorlist[i].text
            timetxt = timelist[i].text
            if('@一键吃书井上葵' in mycontent):
                print ("we got a call at " + timetxt + ", author is: " + author + ", content is:" + mycontent)
                aireturns = self.ch.procCall(mycontent)
                if(len(aireturns) > 0):
                    self.openWriteNewStatus()
                    self.typeWeibo('reply @' + author + ":" + aireturns)
                    return True
        return False
    