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
    
    def getActualResultsNum(self, xpath = "//*[@id='s-result-count']"):
        resultId = "result_"
        if (self.resultNum):
            actualNumResults = self.resultNum - 1
        else:
            actualNumResults = 0
        while (True):
            try:
                item = self.browser.find_element_by_id(resultId + str(actualNumResults))
                actualNumResults += 1
            except NoSuchElementException:
                self.actualResultsNum = actualNumResults
                break
        return actualNumResults
    
    
    def  getItemsWithoutRating(self):
        resultId = "result_"
        cssStr = "#result_"
        cssStr2 = "> div > div > div > div.a-fixed-left-grid-col.a-col-right > div:nth-child(2) > div.a-column.a-span5.a-span-last > div:nth-child(1)"
        nameList = []
        for i in range(self.actualResultsNum):
            item = self.browser.find_element_by_id(resultId + str(i))
            try:
                self.browser.find_element_by_css_selector(cssStr + str(i) + cssStr2)
            except NoSuchElementException:
                nameList.append(item.text)
                
        
        return nameList
    
    def __del__(self):
        self.browser.close()

        
