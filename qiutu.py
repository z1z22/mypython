import urllib.request
import urllib.parse
import os
import time
import re


def handle_request(url, page):
	url = url + str(page) + '/'
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36"}
	print(url)
	request = urllib.request.Request(url = url, headers = headers)
	return request

# <img src="//pic.qiushibaike.com/system/pictures/12151/121511865/medium/MHEGO0YIUCY29MS1.jpg" alt="曾经有一个完整的春节假期摆在我的面前">

def d_img(content):
	pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>', re.S)
	lt = pattern.findall(content)
	for image_src in lt:
		image_src = 'https:' + image_src
		dirname = 'qiutu'
		# print(image_src)
		if not os.path.exists(dirname):
			os.mkdir(dirname)
		filename = image_src.split("/")[-1]
		filepath = dirname + '/' + filename

		print('%s图片正在下载......' %filename)

		urllib.request.urlretrieve(image_src, filepath)
		print('%s下载结束'%filename)
		time.sleep(1)

def main():
	url = 'https://www.qiushibaike.com/pic/page/'
	start_page = int(input('请输入起始页码: '))
	end_page = int(input('请输入结束页码: '))
	for page in range(start_page, end_page + 1):
		print('第%s页开始下载......' %page)
		request = handle_request(url, page)
		content = urllib.request.urlopen(request).read().decode()
		d_img(content)
		print('第%s页下载结束' %page)
		print()
		print()
		time.sleep(2)

if __name__ == '__main__':
	main()