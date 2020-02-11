import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import my2
import os
import urllib.request
import time



def handle_request(url,page = None):
	url = url + str(page) + '.html'
	headers = {	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
	r = requests.get(url=url, headers = headers, timeout = 5)
	return(r)
def list_1(content):
	soup = BeautifulSoup(content,'lxml')
	li_ls = soup.select('.pic > li')
	ls = []
	# print(li_ls)
	for li in li_ls:
		name = li.select('img')[0]['alt']
		href = li.select('a')[0]['href']
		time_ = li.select('.info > span')[1].text
		# print(name)
		# print(href)
		# print(time_)
		img_dict = {
		'name': name,
		'href': 'https://www.mn52.com' + href,
		'time': time_
		}
		ls.append(img_dict)
	return ls

# def img_num(content):
# 	pattern = re.compile(r'<span.*?>(\d\d)</span>') #<span id="totalpage">21</span>
# 	totle_page = pattern.findall(content)
# 	# print(totle_page)
# 	return int(totle_page[-1])
# 	return(totlepage)

def down_img(image_src, dirname):

	# 创建文件名及文件路径
	filename = os.path.basename(image_src)
	filepath = os.path.join(dirname, filename)

	# 使用urlretrieve()添加请求头,注意请求头格式为元组列表
	ua = UserAgent()
	myheaders =  [('User-Agent', ua.random),]
	opener = urllib.request.build_opener()
	opener.addheaders = myheaders
	urllib.request.install_opener(opener)

    # 发送请求下载图片
	urllib.request.urlretrieve(image_src,filepath )
	print('      %s下载结束'%filename)
	time.sleep(1)


def main():
	url = 'https://www.mn52.com/xingganmeinv/list_1_'
	page = input('请输入要下载的页码:')
	r = handle_request(url,page)
	r.encoding = 'utf-8'
	# print(r.text)

	list_img = list_1(r.content)

	n=1
	for img in list_img:
		dname = '['+ img['time'] + ']' + img['name']
		print(dname + '--' + str(n))
		n+=1
	p = int(input('number:'))
	href = list_img[p-1]['href']
	# print(href)
	# exit()
	dirname = '/Volumes/MSDOS/pics/mn53/' + list_img[p-1]['name']
	if not os.path.exists(dirname):
		os.makedirs(dirname)

	# # print(href)
	# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}
		
	# r1 = requests.get(url =img['href'], headers= headers)
	# r1.encoding = 'utf-8'
	# # print(r1.text)
	totalclick = 17#img_num(r1.text)
	ls_src = my2.get_src(href = href,totalclick = totalclick)
	print('开始下载.....')
	for src in ls_src:
		down_img(image_src = src, dirname = dirname)
	print('全部下载结束.')

if __name__ == '__main__':
	main()