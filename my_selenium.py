from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# 详细介绍见博客:
# https://www.cnblogs.com/themost/p/6900852.html

#创建一个参数对象,用来控制chrome以无界面方式运行
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 测试是否成功
path = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(path)
browser.get('https://www.mn52.com/xingganmeinv/23121.html')
time.sleep(3)
butten = browser.find_elements_by_id('photoNext')[0]



# print(butten)
# print(type(butten))
butten.click()
time.sleep(2)
browser.refresh()
# data = browser.page_source
img_src = browser.find_elements_by_xpath('.//div[@class="big-pic"]/div[1]/img')[0]
src = img_src.get_attribute('src')
print(src)
time.sleep(5)

browser.quit()