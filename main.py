# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import configparser
import codecs
import time
import datetime
import random

class CLOCK_IN(object):
    def __init__(self):
        cp = configparser.SafeConfigParser()
        with codecs.open('config.txt', 'r', encoding='utf-8') as f:#读取config.txt数据
            cp.readfp(f)
        self.url=cp.get("data","url")
        self.qq=cp.get("data","qq_num")
        self.name=cp.get("data","name")
        self.driver = webdriver.Chrome("chromedriver.exe")

    def Log_In(self):
        self.driver.get(self.url)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "header-login-btn"))
        )
        element.click()
        #点击 "立即登录"
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("login_frame")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "img_out_"+self.qq))
        )
        element.click()
        #点击快捷登录的头像

    def Change_Page(self):
        self.driver.switch_to.parent_frame()
        time.sleep(3)
        date=str(datetime.datetime.now().month)+"."+str(datetime.datetime.now().day)#生成日期
        while True:
            try:#查看在当前页面是否能找到当前日期的表格
                element = WebDriverWait(self.driver, 2).until(#如果找到则点击
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='"+date+"']"))
                )
                break
            except :
                element = WebDriverWait(self.driver,5).until(#如果没找到则点击右滚动条
                    EC.element_to_be_clickable((By.CLASS_NAME, "sheetscrollright-icon"))
                )
                element.click()
        element.click()
        time.sleep(3)
    
    def Random_Number(self):#生成体温随机数
        return str(random.randint(363,369)/10)

    def Fill_By_Name(self,name):
        elmet = self.driver.find_element_by_id('alloy-simple-text-editor')
        elmet.send_keys(Keys.CONTROL+"f")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search-panel-input"))
        )
        element.click()
        element.send_keys(name)#查找名字
        
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "dui-modal-close"))
        )
        element.click()#退出查找

        for i in range(5):
            time.sleep(0.4)
            elmet.send_keys(Keys.ARROW_RIGHT)

        elmet.click()
        for i in range(5):
            elmet.send_keys(Keys.BACKSPACE)
        elmet.send_keys(self.Random_Number())
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)
        elmet.send_keys(Keys.ARROW_RIGHT)

        elmet.click()
        for i in range(5):
            elmet.send_keys(Keys.BACKSPACE)
        elmet.send_keys(self.Random_Number())
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)
        elmet.send_keys(Keys.ARROW_RIGHT)
        
        elmet.click()
        for i in range(5):
            elmet.send_keys(Keys.BACKSPACE)
        elmet.send_keys("1")
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)
        elmet.send_keys(Keys.ARROW_RIGHT)

        elmet.click()
        for i in range(5):
            elmet.send_keys(Keys.BACKSPACE)
        elmet.send_keys(self.Random_Number())
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)
        elmet.send_keys(Keys.ARROW_RIGHT)

        elmet.click()
        for i in range(5):
            elmet.send_keys(Keys.BACKSPACE)
        elmet.send_keys("1")
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)
        elmet.send_keys(Keys.ARROW_RIGHT)

    def Run(self):
        names=self.name.split()
        for i in names:
            self.Fill_By_Name(i)

if __name__ == "__main__":
    my_clock = CLOCK_IN()
    my_clock.Log_In()
    my_clock.Change_Page()
    my_clock.Run()