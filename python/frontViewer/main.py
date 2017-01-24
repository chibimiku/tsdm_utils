#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time,os,traceback,urllib.parse

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class WindowsDriver:
    
    def __init__(self):
    
        self.loadpageTimeout=5000
        self.waitAfterOperation=1.5 #操作后等1秒
        self.waitAfterBigOperation=5 #比较耗时的操作后等5秒
    
        chromedriverPath='lib/chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = chromedriverPath
        self.driver = webdriver.Chrome(chromedriverPath)
        self.driver.set_page_load_timeout(self.loadpageTimeout)
        self.plog ("Driver started...")
    
    def runFetch(self):
        #just for test.
        self.driver.get('http://www.baidu.com/')
        self.driver.quit()
        
if __name__=='__main__':
    wwd = WindowsWebDriver()
    wwd.runFetch()