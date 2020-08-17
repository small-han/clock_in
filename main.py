from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import datetime

class CLOCK_IN(object):
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.row = 1
        self.col = 1

    def Log_In(self, url):
        self.driver.get(url)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "header-login-btn"))
        )
        element.click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("login_frame")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "img_out_1392104628"))
        )
        element.click()

    def Fill_In(self, row, col, data):
        elmet = self.driver.find_element_by_id('alloy-simple-text-editor')
        if self.row-row > 0:
            for i in range(self.row-row):
                time.sleep(0.1)
                elmet.send_keys(Keys.ARROW_UP)
        elif self.row-row < 0:
            for i in range(row-self.row):
                time.sleep(0.1)
                elmet.send_keys(Keys.ARROW_DOWN)
        if self.col-col > 0:
            for i in range(self.col-col):
                time.sleep(0.1)
                elmet.send_keys(Keys.ARROW_LEFT)
        elif self.col-col < 0:
            for i in range(col-self.col):
                time.sleep(0.1)
                elmet.send_keys(Keys.ARROW_RIGHT)
        elmet.click()
        for i in range(5):
            elmet.send_keys(Keys.BACKSPACE)
        elmet.send_keys(data)
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)
        self.row=row
        self.col=col

    def Change_Page(self):
        #element= self.driver.find_element_by_partial_link_text("sheet-tab-name")
        self.driver.switch_to.parent_frame()
        # self.driver.implicitly_wait(10)
        time.sleep(5)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8.15']"))
        )
        element.click()

    def Fill_Ones_Message(self,row):
        self.Fill_In(row,6,"36.7")
        self.Fill_In(row,7,"36.7")
        self.Fill_In(row,8,"1")
        self.Fill_In(row,9,"36.7")
        self.Fill_In(row,10,"1")
    
    def test(self):
        elmet = self.driver.find_element_by_id('alloy-simple-text-editor')
        """
        for i in range(117):
            elmet.send_keys(Keys.ARROW_DOWN)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='117']"))
        )
        element.click()
        """
        elmet.send_keys(Keys.CONTROL+"f")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search-panel-input"))
        )



if __name__ == "__main__":
    my_clock = CLOCK_IN()
    my_clock.Log_In("https://docs.qq.com/sheet/DRUt0S0VnSEZKU3hV?tdsourcetag=s_pcqq_send_grpfile&ADUIN=1392104628&ADSESSION=1597489369&ADTAG=CLIENT.QQ.5749_.0&ADPUBNO=27027&tab=jiwl0l")
    my_clock.Change_Page()
    my_clock.test()
"""
    my_clock.Fill_Ones_Message(171)
    my_clock.Fill_Ones_Message(190)
"""
