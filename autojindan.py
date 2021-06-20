# -*- coding: utf-8 -*-
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys as K
import time
import sys

password = input("자가진단 비밀번호 입력 : ")

b = wb.Chrome('C:/chromedriver_win32/chromedriver.exe')
b.get("https://hcs.eduro.go.kr/#/relogin")

def login():

    time.sleep(1)
    b.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="sidolabel"]/option[text()="서울특별시"]').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="crseScCode"]/option[text()="고등학교"]').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="orgname"]').send_keys("서울고등학교")
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a/p/a').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="user_name_input"]').send_keys("김홍순")
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="birthday_input"]').send_keys('050508')
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys(password)
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(1)

def jindan():
    time.sleep(2)
    b.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
    time.sleep(1)
    b.find_element_by_xpath('//*[@id="btnConfirm"]').click()

login()
jindan()






