import requests
import json

post_url = 'https://fanyi.baidu.com/sug'
word =  input('请输入要查询的单词: ')

form_data = {
    'kw': word,
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

response = requests.post(post_url, headers = headers,data = form_data )


js = response.json()
print(js)


with open('baidu_fanyi.txt', 'a') as ft:
    js_data = js['data']
    for i in js_data:
        k = i['k'] + ' : ' + i['v']
        print (k)
        ft.write('\n'+k)
print('查询完成,文件已写入baidu_fanyi.txt')


