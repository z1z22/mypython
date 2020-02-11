
import urllib.request
import urllib.parse
import os
import time
from lxml import etree
import re
import random
from fake_useragent import UserAgent
import inputdigit



def handle_request(url, page = None):
	'''构建发送请求,返回request'''
	if page == None or page == 1:
		url = url
	else:
		url = url + str(page) + '.html'
	# print(url)
	#创建随机请求头
	ua = UserAgent()
	headers = {'User-Agent': ua.random}
	# print(url)
	request = urllib.request.Request(url = url, headers = headers)
	return request


def img_src(content):
    '''提取图片地址,返回图片名称日期及地址列表'''
    tree = etree.HTML(content)
    li_list = tree.xpath('//ul[@class="ulPic"]/li')
    # print(li_list)
    # print(len(li_list))
    item_ls = []
    num = 1
    for li in li_list:
    	href = li.xpath('.//a/@href')[0]
    	dirname = li.xpath('.//a/i[@class="tit"]/text()')[0]
    	item = {'num':num, 'dirname': dirname, 'href': href}
    	item_ls.append(item)
    	num += 1
    return item_ls


def img_nums(content):
		# 匹配字段确定每组图片张数
	pattern = re.compile(r'<a.*?>(\d{2,3})</a>\s<a.*?' ,re.S) 
	totle_page = pattern.findall(content)
	return totle_page[0]


def down_img(content,dirname):
	'''下载图片到指定目录'''
	tree = etree.HTML(content)
	image_src_ls1= tree.xpath('.//div[@class="main"]/div[2]/a/img/@src')
	image_src_ls2= tree.xpath('.//div[@class="main"]/div[3]/a/img/@src')
	image_src_ls3= tree.xpath('.//div[@class="main"]/div[4]/a/img/@src')

	image_src_ls = image_src_ls1 + image_src_ls2 + image_src_ls3
	ua = UserAgent()
	myheaders =  [('User-Agent', ua.random)]
	opener = urllib.request.build_opener()
	opener.addheaders = myheaders
	urllib.request.install_opener(opener)
	# print(image_src_ls)
	for image_src in image_src_ls:
		# 创建文件名及文件路径
		filename = os.path.basename(image_src)
		filepath = os.path.join(dirname, filename)
		# 发送请求下载图片
		print (image_src)
		urllib.request.urlretrieve(image_src, filepath)
		print('      %s下载结束'%filename)
		time.sleep(random.randint(1,3))


def main():
	'''根据输入的页码,下载9rti中图片'''
	url = 'http://www.9rti.com/html/guomosipai/'
	page = inputdigit.inputdigit('请输入下载页码: ')
	request = handle_request(url, page)
	content = urllib.request.urlopen(request).read().decode('gbk')
	url_list = img_src(content)
	totle = len(url_list)
	# print (totle)
	for list in url_list:
		print (str(list['num'])+list['dirname'])
	print('第%d页共有%d套' %(page, totle))
	zone = inputdigit.inputdigit('请输入下载部分: ')
	l = 0
	zone_ind = zone-1
	image = url_list[zone_ind]
	#根据图片名称及日期创建图片目录
	dirname = 'rtystp/' + image['dirname']
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	href = 'http://www.9rti.com/' + image['href']
	request = handle_request(url = href)
	content = urllib.request.urlopen(request).read().decode('gbk')
	print('%s正在下载......' %(image['dirname']))
	totle_page = img_nums(content)
	# print(totle_page)
	m = 0
	for img_page in range(1, int(totle_page)+1):
		if img_page == 1:
			img_url = href
		else:
			page_string = '_' + str(img_page) + '.html'
			img_url = href.replace('.html',page_string)
		# print(img_url)
		request = handle_request(img_url)
		content = urllib.request.urlopen(request).read().decode('gbk')
		m += 1
		l += 1
		print('第(%d/%s)页正在下载(总第%d页)......' %(m, totle_page, l))
		down_img(content, dirname)
  	# print('第%d套下载结束' %zone）

if __name__ == '__main__':
	main()