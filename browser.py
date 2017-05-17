#!/usr/bin/env python3
import os
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
class browser:
    def __init__(self, browserType = 'chrome', driverPath = 'C:\chromedriver'):
        if (browserType == 'chrome'):
            os.environ["webdriver.chrome.driver"] = driverPath
            self.type = browserType
            self.browser = webdriver.Chrome(driverPath)
        else:
            print ("Unsupported Browser")
            return 0
        
    def openUrl(self, url = 'https://amazon.com/'):
        self.browser.get(url)
        
        
    def search(self, strSearch = "Ender\'s Game", searchId = "twotabsearchtextbox"):
        element = self.browser.find_element_by_id(searchId)
        element.clear()
        element.send_keys(strSearch + Keys.RETURN)
        assert "No results found." not in self.browser.page_source
        
    def getResultsNum(self,xpath = "//*[@id='s-result-count']" ):
        textData = self.browser.find_element_by_xpath(xpath)
        if(textData.text == False):
            return 
        tmp = re.search('\d+-(\d+)',textData.text)
        if (tmp):
            self.resultNum = int(tmp.group(1))
            return self.resultNum
        return 0
    
    def getResulstList(self,cssStr = "result_" ):
        self.elements = self.browser.find_elements_by_css_selector('[id*="%s"]' % cssStr)
        self.actualResultsNum = len(self.elements)
        return self.elements
    
    def getActualResultsNum(self):
        return self.actualResultsNum
    
    
    def  getItemsWithoutRating(self):
        nameList = []
        for item in self.elements:
            try:
                item.find_element_by_class_name('a-icon-alt')
            except NoSuchElementException:
                nameList.append(item.text)
        return nameList
    
    def close(self):
        if(self.browser):
            self.browser.close()
            self.browser = 0
    
    def __del__(self):
        self.close()
        
