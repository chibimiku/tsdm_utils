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
        el = self.driver.find_element_by_id('form_textarea')
        #el.send_keys(Keys.CONTROL, 'v') #Parse.
        el.send_keys(content)
        mybtn = self.driver.find_element_by_class_name('fr txt-link')
        mybtn.click()
        