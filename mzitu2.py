import urllib.request
import urllib.parse
import os
import time
from lxml import etree
import re
import random
from fake_useragent import UserAgent


def handle_request(url, page = None):
	'''构建发送请求,返回request'''
	if page == None:
		url = url
	else:
		url = url + str(page) + '/'

	ua = UserAgent()
	headers = {'User-Agent': ua.random}
	# print(url)
	request = urllib.request.Request(url = url, headers = headers)
	return request


def img_src(content):
	'''提取图片地址,返回图片名称日期及地址列表'''
	tree = etree.HTML(content)
	li_list = tree.xpath('//ul[@id="pins"]/li')
	# print(li_list)
	# print(len(li_list))
	item_ls = []
	for li in li_list:
	    href = li.xpath('.//span/a/@href')[0]
	    dirname = li.xpath('.//span/a/text()')[0]
	    _time = li.xpath('.//span[@class="time"]/text()')[0]
	    item = {
	    'time': _time,
	    'dirname':dirname,
	    'href':href
	    }
	    item_ls.append(item)
	return item_ls


def img_nums(content):
		# 匹配字段确定每组图片张数
	pattern = re.compile(r'<span>(\d\d)</span>') 
	totle_page = pattern.findall(content)
	return totle_page[0]
		

def down_img(content,dirname):
	'''下载图片到指定目录'''

	tree = etree.HTML(content)
	image_src = tree.xpath('.//div[@class="main-image"]/p/a/img/@src')[0]

	# 创建文件名及文件路径
	filename = os.path.basename(image_src)
	filepath = os.path.join(dirname, filename)

	# 为使用urlretrieve()添加请求头,注意请求头格式为元组列表
	ua = UserAgent()
	myheaders =  [
	('Referer', 'https://www.mzitu.com'),
	('Upgrade-Insecure-Requests', '1'),
	('User-Agent', ua.random),
	]
	opener = urllib.request.build_opener()
	opener.addheaders = myheaders
	urllib.request.install_opener(opener)

    # 发送请求下载图片
	urllib.request.urlretrieve(image_src,filepath )
	print('%s下载结束'%filename)
	time.sleep(random.randint(1,3))


def main():
	'''根据输入的页码,下载mzitu中图片'''
	url = 'https://www.mzitu.com/page/'
	page = int(input('请输入下载页码(每页约1000张): '))
	zone = input('请输入下载部分四分之: ')#一页图片太多,分为四组
	print('第%s页开始下载......' %page)
	request = handle_request(url, page)
	content = urllib.request.urlopen(request).read().decode()
	url_list = img_src(content)

	totle = len(url_list)
	n, l = 0 , 0
	
	if zone == '1':
		a, b = 0, 7
	if zone == '2':
		a, b = 7, 13
	if zone == '3':
		a, b = 13, 19
	if zone == '4':
		a, b = 19, -1

	for image in url_list[a:b]:

    	#根据图片名称及日期创建图片目录
		dirname = '/Volumes/APFS_Disk/meizi/[' + image['time']+ ']' + image['dirname']
		if not os.path.exists(dirname):
			os.makedirs(dirname)

		href = image['href']
		n += 1
		#发送请求获取每组图片总张数
		request = handle_request(href)
		content = urllib.request.urlopen(request).read().decode()
		print('(第%d组/共%d组)%s正在下载......' %(n, totle, image['dirname']))
		totle_page = img_nums(content)
		
		m = 0
		for page in range(1, int(totle_page)+1):
			img_url = href + '/' + str(page)
			# print(img_url)
			request = handle_request(img_url)
			content = urllib.request.urlopen(request).read().decode()
			m += 1
			l += 1
			print('(%d/%d)组(%d/%s)张正在下载(总第%d张)......' %(n, totle, m, totle_page, l))
			down_img(content, dirname)
		print('第%d组下载结束' %n)
	print('第%d页下载结束' %page)

if __name__ == '__main__':
	main()