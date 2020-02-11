import urllib.request
import urllib.parse
import json
from lake_useragent import User_Agent

post_url = 'https://fanyi.baidu.com/v2transapi'

word = input('查询的单词: ')

ua = User_Agent()
form_data = {
	'from': 'en',
    'to': 'zh',
    'query': word,
    'transtype': 'realtime',
    'simple_means_flag': 3,
    'sign': 814534.560887,
    'token': '39ee19e329ed942eb4d5e84270958c4c',
}
headers = {
    'Host': 'fanyi.baidu.com',
    'Connection': 'keep-alive',
    'Content-Length': 117,
    'Accept': '*/*',
    'Origin': 'https://fanyi.baidu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': ua.random,
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    #Accept-Encoding: gzip, deflate, br
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BAIDUID=D23A98BB001ECFD83091C34CC5D80281:FG=1; BIDUPSID=D23A98BB001ECFD83091C34CC5D80281; PSTM=1548603480; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1548603485,1548690010,1548740949; H_PS_PSSID=1454_21079_28328_28414; delPer=0; PSINO=1; locale=zh; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1548749740',
}
request = urllib.request.Request(url = post_url, headers =headers)

form_data = urllib.parse.urlencode(form_data).encode()

response = urllib.request.urlopen(request,data =form_data )

json_str = response.read().decode()
print(json.loads(json_str))

type(json.loads(json_str))