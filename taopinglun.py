import urllib.request as ur
from lxml import etree
from fake_useragent import UserAgent
import inputdigit
import json

def texts(content):
	tree = etree.HTML(content)
	user_div_ls = tree.xpath('//div[@class="rv-target-item"]/div')
	# print(user_div_ls)
	user_c_ls = []
	for user_div in user_div_ls:
		# print(user_div)
		username = user_div.xpath('.//div[@class="username"]/span/text()')[0]
		texts = user_div.xpath('.//p[@class="body-content"]/text()')[0].strip()
		texts_zhui =  user_div.xpath('.//div[@class="content"]/p/text()')
		if texts_zhui == []:
			texts_zhui = 'No'
		else:
			texts_zhui = texts_zhui[0].strip()
		datetime = user_div.xpath('.//div[@class="date l"]//span/text()')[0]
		# print(username)
		# print(texts)
		# print(texts_zhui)
		# print(datetime)
		user_comment = {
		'用户名':username,
		'评论时间':datetime,
		'内容':texts,
		'追评内容':texts_zhui
		}
		user_c_ls.append(user_comment)
	return user_c_ls



def handle_request(url,page):
	url = url + str(page) + '-total.htm'
	ua = UserAgent()
	headers = {'User-Agent': ua.random}
	request = ur.Request(url, headers = headers)
	return request

def store_text(texts):
	strings = json.dumps(texts, ensure_ascii = False)
	with open('snygpl2.json','w',encoding = 'utf8') as fp:
		fp.write(strings)


	

def main():
	url = 'https://review.suning.com/cluster_cmmdty_review/style--000000000693107443-0070097684-'
	page_start = inputdigit.inputdigit('page_start:')
	page_end = inputdigit.inputdigit('page_end:')
	comment_list = []
	for page in range(page_start-1, page_end):
		request = handle_request(url,page)
		content = ur.urlopen(request).read().decode()

		comment_list += texts(content)
	store_text(comment_list)
	print('下载苏宁评论完成')

if __name__ == '__main__':
	main()
