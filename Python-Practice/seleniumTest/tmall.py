#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def login_taobao():
    """
    登陆淘宝功能
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    # driver.maximize_window() #将浏览器最大化显示
    driver.delete_all_cookies()
    driver.get("https://login.taobao.com/member/login.jhtml")
    #load the switch
    element = driver.find_element_by_xpath("//*[@id='J_Quick2Static']")
    element.click()
    driver.implicitly_wait(20)
    username=driver.find_element_by_name("TPL_username")
    if not username.is_displayed:
        driver.implicitly_wait(20)
        driver.find_element_by_xpath("//*[@id='J_Quick2Static']").click()
    driver.implicitly_wait(20)
    username.send_keys("qiumy23")
    driver.find_element_by_name("TPL_password").send_keys("equa5T6ing")
    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//*[@id='J_SubmitStatic']").click()
    # time.sleep(4)
    # driver.quit()
    return driver

def testTmall(url, choices):
	# driver = webdriver.Chrome()
	driver = login_taobao()
	driver.get(url)
	# driver.implicitly_wait(10)
	try:
		for choice in choices:
			ele = driver.find_element_by_partial_link_text(choice)
			if "已选择" not in ele.get_attribute("aria-label"):
				ele.click()

		buyBtn = driver.find_element_by_partial_link_text('立即购买')

		while True:
			if buyBtn.is_displayed():
				buyBtn.click()
				break
		# time.sleep(3)

		submit = driver.find_element_by_partial_link_text("提交订单")
		submit.click()
		time.sleep(1100)
		print("下单成功")
	except Exception as e:
		print(e)
	driver.quit()

if __name__ == '__main__':
	# login_taobao()
	url = "https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w13632750-16055773094.40.UHWajY&id=545034692230&scene=taobao_shop&skuId=3455116798528"
	choices = ["4G全网通", "极光蓝","官方标配", "64GB"]
	testTmall(url, choices)