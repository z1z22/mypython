from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

#创建一个参数对象,用来控制chrome以无界面方式运行
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 测试是否成功,创建浏览器对象
path = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(executable_path = path,chrome_options=chrome_options)

def get_src(href,totalclick):
	print('正在使用selemium解析网页......')
	src_list = []
	browser.get(href)
	time.sleep(1)
	browser.refresh()
	time.sleep(5)
	img_src = browser.find_elements_by_xpath('.//div[@class="big-pic"]/div[1]/img')[0]
	src = img_src.get_attribute('src')
	src_list.append(src)
	print('正在提取链接,请耐心等待....')
	for i in range(0,totalclick):
		butten = browser.find_elements_by_id('photoNext')[0]
		butten.click()
		time.sleep(2)
		browser.refresh()
		img_src = browser.find_elements_by_xpath('.//div[@class="big-pic"]/div[1]/img')[0]
		src = img_src.get_attribute('src')
		print(src)
		src_list.append(src)
	browser.quit()	
	return(src_list)