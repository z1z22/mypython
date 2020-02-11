import requests, os,time,random
import pymongo
from fake_useragent import UserAgent
from retrying import retry

def _result(result):
	return result is None

@retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
def handle_requests(url, page = None, Referer = None):
	'''构建发送请求,返回requests'''
	if page:
		url = url + str(page) + '/'
	#创建随机请求头
	# ua = UserAgent()
	proxie_list = [
	 'http://116.209.55.225:9999',
	 'http://116.209.55.252:9999', 
	 'http://111.177.179.54:9999', 
	 'http://121.40.138.161:8000', 
	 'http://110.52.235.19:9999', 
	 'http://111.177.191.109:9999', 
	 'http://117.87.178.114:9000', 
	 'http://116.209.59.223:9999', 
	 'http://47.94.57.119:80', 
	 'http://47.94.57.119:80', 
	 'http://47.96.135.84:80', 
	 'http://117.191.11.107:8080', 
	 'http://121.33.255.219:80', 
	 'http://123.56.11.19:80', 
	 'http://60.13.42.158:9999', 
	 'http://117.191.11.79:8080', 
	 'http://18.223.141.123:80', 
	 'http://211.136.127.125:80'
	 ]
	# proxies = {
 # 		"http": random.choice(proxie_list)
	# }
	ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
	headers = {'User-Agent': ua}
	# headers = {'User-Agent': ua.random,}
	if Referer is not None:

		headers['Referer'] = Referer
		print(headers)

	r = requests.get(
		url = url, 
		headers = headers, 
		proxies={
 		"http": random.choice(proxie_list)
	}, 
		timeout = 10,
		)
	if r.status_code !=200:
		raise requests.RequestException('my_request_get error!!!!')
	return r


def mongodb_join(db_name,col_name):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")#创建数据库
	mydb = myclient[db_name] #创建数据库
	mycol = mydb[col_name] #创建集合
	# for item in mycol.find({'dirname':{'$regex':'爱丝'}},{'_id':0}).sort('picname', pymongo.ASCENDING):
	for item in mycol.find({},{'_id':0}).limit(1000).skip(14000):#.sort('picname', pymongo.ASCENDING):
		# print(item)
		download_pic(item)
		time.sleep(1)

def download_pic(pic_item):
	dirpath = '/Volumes/MSDOS/mongopics/' + '/'.join(pic_item['picstore'].split('/')[:-1]).replace(' ','')
	picpath = '/Volumes/MSDOS/mongopics/' + pic_item['picstore'].replace(' ','')
	print(dirpath)
	print(picpath)

	# dirpath = '/Users/mac/python/girl_scrapy/' + '/'.join(pic_item['picstore'].split('/')[:-1]).replace(' ','')
	# picpath = '/Users/mac/python/girl_scrapy/' + pic_item['picstore'].replace(' ','')



	if not os.path.exists(dirpath):
		os.makedirs(dirpath)

	elif os.path.exists(picpath):
		print('{}已存在.'.format(pic_item['picname']))
		return
	# ua = UserAgent()
	# headers = {'User-Agent': ua.random,
	# 'Referer': pic_item['Referer'],
	# }
	print(pic_item['src'])
	print(pic_item['Referer'])
	# r = requests.get(url, headers = headers, timeout = (3, 7))
	r = handle_requests(pic_item['src'], Referer=pic_item['Referer'])

	with open(picpath, 'wb') as fp:
			fp.write(r.content)
	print('{} is downloaded.'.format(pic_item['picname']))

def main():
	db_name = 'scrapy_db'#input('dbname: ')
	col_name = 'girlsofdesire'#input('collection:')
	mongodb_join(db_name, col_name)



	
if __name__ == '__main__':
	main()