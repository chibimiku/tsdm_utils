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
    
        mobileua = 'Mozilla/5.0 (Linux; U; Android 6.0.1; zh-tw; E5823 Build/32.2.A.0.305) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.2 Mobile Safari/537.36';
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--user-agent=" + mobileua)
    
        chromedriverPath='lib/chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = chromedriverPath
        self.driver = webdriver.Chrome(chromedriverPath, chrome_options=chrome_options)
        self.driver.set_page_load_timeout(self.loadpageTimeout)
        self.plog ("Driver started...")
    
    def runFetch(self):
        #just for test.
        self.driver.get('http://www.baidu.com/')
        self.driver.quit()
        
if __name__=='__main__':
    mydriver = WindowsDriver()
    mydriver.runFetch()