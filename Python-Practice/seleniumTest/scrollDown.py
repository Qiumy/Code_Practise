#coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.cnbc.com/finance/')
time.sleep(3)
for i in range(10):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    print("page Down: ", i)
    time.sleep(5)