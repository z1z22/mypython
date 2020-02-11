import time
import requests
import json

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=%d' %int(time.time()*1000)

data = json.loads(requests.get(url=url).json()['data'])
print(len(data))
print(data[0])