#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def testBaidu():
	driver = webdriver.Chrome()
	driver.get("https://www.baidu.com")

	driver.find_element_by_id('kw').send_keys("selenium")
	driver.find_element_by_id('su').click()

	driver.quit()

def findEle():
	driver = webdriver.Chrome()
	driver.get("http://sahitest.com/demo/linkTest.htm")
	driver.implicitly_wait(10)

	# driver.set_window_size(400, 800)

	# element = driver.find_element_by_id("dragger")
	# target = driver.find_elements_by_class_name("item")
	# actions = ActionChains(driver)
	# actions.drag_and_drop(element, target[1]).perform()

	# time.sleep(4)
	# driver.quit()

	# driver.find_element_by_name('b1').click()
	# time.sleep(4)
	# driver.switch_to_alert().dismiss()
	# time.sleep(4)
	# driver.quit()
	link = driver.find_element_by_link_text("linkByContent")
	link.click()

	time.sleep(4)
	back = driver.find_element_by_link_text("Back")
	back.click()
	time.sleep(4)
	driver.quit()

if __name__ == '__main__':
	findEle()