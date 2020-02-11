import requests,time
# from retrying import retry

from lxml import etree


def request_handler(url):
	print(url)
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

	r = requests.get(url,headers = headers,timeout = 1)

	return r
def parse(content):
	tree = etree.HTML(content)
	proxy_list = []
	daili_list = tree.xpath('//div[@id="list"]/table/tbody/tr')
	for tr in daili_list:
		daili_ip = tr.xpath('./td[@data-title="IP"]/text()')
		daili_post = tr.xpath('./td[@data-title="PORT"]/text()')
		daili_type = tr.xpath('./td[@data-title="类型"]/text()')

		proxy = '{}://{}:{}'.format(daili_type[0].lower(),daili_ip[0],daili_post[0])
		proxy_list.append(proxy)
		# print(daili_ip,daili_post,daili_type)
	return proxy_list
def check_proxy(proxy_list):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}	
	url = "http://www.baidu.com/"
	normal_proxies = []
	for proxy in proxy_list:
		try:
			r = requests.get(url, headers=headers, proxies={"http": proxy}, timeout=1)
			# print(r.status_code )
			if r.status_code == 200:
				print("该代理IP可用：", proxy)
				normal_proxies.append(proxy)
			else:
				print("该代理IP不可用：", proxy)
		except Exception:
			print("该代理IP无效：", proxy)
			pass
	return normal_proxies

def main():
	baseurl = 'https://www.kuaidaili.com/free/inha/{}/'
	prixypool = []
	for page in range(1,100):
		url = baseurl.format(page)
		r = request_handler(url)
		proxy_list = parse(r.text)
		# print(proxy_list)
		prixies = check_proxy(proxy_list)
		# print(prixies)
		prixypool = prixypool + prixies
		time.sleep(1)
	print(prixypool)
	prixypool2 = check_proxy(prixypool)
	print(prixypool2)




if __name__ == '__main__':
	main()