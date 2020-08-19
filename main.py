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
        with codecs.open('config.txt', 'r', encoding='utf-8') as f:
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
        self.driver.implicitly_wait(2)
        self.driver.switch_to.frame("login_frame")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "img_out_"+self.qq))
        )
        element.click()

    def Change_Page(self):
        self.driver.switch_to.parent_frame()
        time.sleep(3)
        date=str(datetime.datetime.now().month)+"."+str(datetime.datetime.now().day)
        while True:
            try:
                element = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='"+date+"']"))
                )
                break
            except :
                element = WebDriverWait(self.driver,5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "sheetscrollright-icon"))
                )
                element.click()
        element.click()
    
    def Random_Number(self):
        return str(random.randint(363,369)/10)

    def Fill_By_Name(self,name):
        elmet = self.driver.find_element_by_id('alloy-simple-text-editor')
        elmet.send_keys(Keys.CONTROL+"f")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search-panel-input"))
        )
        element.click()
        element.send_keys(name)
        
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "dui-modal-close"))
        )
        element.click()

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