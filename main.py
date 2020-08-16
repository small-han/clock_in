from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import datetime
# 填写腾讯文档
class CLOCK_IN(object):
    def __init__(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        pass

    def Log_In(self,url):
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

    def Fill_In(self,row,col,data):
        self.driver.switch_to.parent_frame() 
        elmet = self.driver.find_element_by_id('alloy-simple-text-editor')
        elmet.click()
        elmet.send_keys(Keys.ESCAPE)
        for i in range(row-1):
            elmet.send_keys(Keys.ARROW_DOWN)
        for i in range(col-1):
            elmet.send_keys(Keys.ARROW_RIGHT)
        elmet.click()
        elmet.send_keys(data)   # 输入xxx,即你想输入的字符
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)
        
        elmet.send_keys(Keys.ARROW_RIGHT)
        elmet.click()
        elmet.send_keys("36.7")   # 输入xxx,即你想输入的字符
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)


        elmet.send_keys(Keys.ARROW_RIGHT)
        elmet.click()
        elmet.send_keys("1")   # 输入xxx,即你想输入的字符
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)

        elmet.send_keys(Keys.ARROW_RIGHT)
        elmet.click()
        elmet.send_keys("36.7")   # 输入xxx,即你想输入的字符
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)

        elmet.send_keys(Keys.ARROW_RIGHT)
        elmet.click()
        elmet.send_keys("1")   # 输入xxx,即你想输入的字符
        elmet.send_keys(Keys.ENTER)
        elmet.send_keys(Keys.ARROW_UP)
        """
        for i in range(row-1):
            elmet.send_keys(Keys.ARROW_UP)
        for i in range(col-1):
            elmet.send_keys(Keys.ARROW_LEFT)
        """

    def Change_Page(self):
        #element= self.driver.find_element_by_partial_link_text("sheet-tab-name")
        self.driver.switch_to.parent_frame() 
        #self.driver.implicitly_wait(10)
        time.sleep(5)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='8.14']"))
        )
        element.click()

if __name__ == "__main__" :
    my_clock=CLOCK_IN()
    my_clock.Log_In("https://docs.qq.com/sheet/DRUt0S0VnSEZKU3hV?tdsourcetag=s_pcqq_send_grpfile&ADUIN=1392104628&ADSESSION=1597489369&ADTAG=CLIENT.QQ.5749_.0&ADPUBNO=27027&tab=jiwl0l")
    my_clock.Change_Page()
    my_clock.Fill_In(171,6,"36.7")
    """
    my_clock.Fill_In(171,7,"36.7")
    my_clock.Fill_In(171,8,"1")
    my_clock.Fill_In(171,9,"36.7")
    my_clock.Fill_In(171,10,"1")
    """
    #my_clock.Fill_In(3,6,"hello")
    print("hello")
     