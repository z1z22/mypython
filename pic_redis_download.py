import requests, os,time
import pymongo
from fake_useragent import UserAgent
from retrying import retry
from redis import Redis

# redis_connect = Redis.from_url("redis://127.0.0.1:6379", decode_responses=True)
poor = Redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r =Redis(connection_pool=poor)
def setredis(url)
	r.sadd('novohot:urls':url)
	# print(r.get('novohot:requests'))

def _result(result):
	return result is None

@retry(stop_max_attempt_number=5, wait_random_min=1000, wait_random_max=2000, retry_on_result=_result)
def handle_requests(url, page = None):
	'''构建发送请求,返回requests'''
	if page:
		url = url + str(page) + '/'
	#创建随机请求头
	ua = UserAgent()
	headers = {'User-Agent': ua.random}
	r = requests.get(url = url, headers = headers, allow_redirects=False, timeout = 5)
	if r.status_code !=200:
		raise requests.RequestException('my_request_get error!!!!')
	return r


def mongodb_join(db_name,col_name):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")#创建数据库
	mydb = myclient[db_name] #创建数据库
	mycol = mydb[col_name] #创建集合
	# for item in mycol.find({'dirname':{'$regex':'爱丝'}},{'_id':0}).sort('picname', pymongo.ASCENDING):
	for item in mycol.find({},{'_id':0}).sort('picname', pymongo.ASCENDING).limit(1000):
		print(item)
		# setredis(item['src'])
		r.sadd('novohot:urls':url)
		pic_src = r.spop('novohot:urls')


		download_pic(item)
		time.sleep(1)

def download_pic(pic_item,pic_src):
	dirpath = '/Volumes/MSDOS/mongopics/' + '/'.join(pic_item['picstore'].split('/')[:-1]).replace(' ','')
	picpath = '/Volumes/MSDOS/mongopics/' + pic_item['picstore'].replace(' ','')

	if not os.path.exists(dirpath):
		os.makedirs(dirpath)

	elif os.path.exists(picpath):
		print('{}已存在.'.format(pic_item['picname']))
		return
	# ua = UserAgent()
	# headers = {'User-Agent': ua.random,
	# 'Referer': pic_item['Referer'],
	# }
	url = pic_item['src']
	print(url)
	# r = requests.get(url, headers = headers, timeout = (3, 7))
	r = handle_requests(url)

	with open(picpath, 'wb') as fp:
			fp.write(r.content)
	print('{} is downloaded.'.format(pic_item['picname']))

def main():
	db_name = 'scrapy_db'#input('dbname: ')
	col_name = input('collection:')
	mongodb_join(db_name, col_name)



	
if __name__ == '__main__':
	main()