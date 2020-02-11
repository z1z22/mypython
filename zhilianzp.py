from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

browser = webdriver.Chrome('/usr/local/bin/chromedriver')

headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
def browser_seleniun(url):
	browser.get(url)
	time.sleep(5)
	browser.refresh()
	time.sleep(5)
	r = browser.page_source
	browser.quit()
	return r



def parse_text(content):
	soup = BeautifulSoup(content,'lxml')

	div_ls = soup.select('#listItemPile')
	print (content)


https://sou.zhaopin.com?/c/i/sou?start=90&pageSize=90&cityId=%E5%8C%97%E4%BA%AC&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=java&kt=3&=0&_v=0.65293545&x-zp-page-request-id=c7fbf676eb544df684b74110302baff2-1551926837280-959249

def main():
	# url = 'https://sou.zhaopin.com'
	url = 'https://sou.zhaopin.com/?'
	jl = '北京'#input('请输入工作地点: ')
	kw = 'java'#input('请输入工作关键字: ')
	start_page = 1#int(input('请输入起始页码: '))
	end_page = 1#int(input('请输入结束页码: '))
# https://sou.zhaopin.com/?jl=%E5%8C%97%E4%BA%AC&kw=java&kt=3&sf=0&st=0
	for page in range(start_page,end_page + 1):
		url = url + 'p={}&jl={}&kw={}'.format(page,jl,kw)
		r = browser_seleniun(url)
		print(r)

		# mylist = parse_text(r.text)





if __name__ == '__main__':
	main()
