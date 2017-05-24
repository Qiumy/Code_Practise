#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import taobao

def testTmall(url, choices):
	driver = webdriver.Chrome()
	driver.get(url)
	try:
		for choice in choices:
			ele = driver.find_element_by_partial_link_text(choice)
			if "已选择" not in ele.get_attribute("aria-label"):
				ele.click()

		buyBtn = driver.find_element_by_partial_link_text('立即购买')

		if buyBtn.is_displayed():
			buyBtn.click()
		time.sleep(3)
	except Exception as e:
		print(e)
	driver.quit()

if __name__ == '__main__':
	tmall = taobao.Taobao()
	tmall.main()
	url = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.KWDnGm&id=522566492692&skuId=3111068604442&areaId=440100&user_id=2074649025&cat_id=2&is_b=1&rn=cd38cac8af79656a668c1634898cd1cb"
	choices = ["S", "03蓝白"]
	testTmall(url, choices)