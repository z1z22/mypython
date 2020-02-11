import urllib.request
import urllib.parse
import os


# 输入吧名,开始页,结束页.然后在当前文件夹中创建一个以吧名为名字的文件夹,里面是每一页的html内容,文件名是页码数.

ba_name = input('吧名: ')
start_page = int(input('起始页码: '))
end_page = int(input('结束页吗: '))

# 创建文件夹
if not os.path.exists(ba_name):
    os.mkdir(ba_name)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# https://tieba.baidu.com/f?ie=utf-8&kw=美女&pn=50
url = 'https://tieba.baidu.com/f?ie=utf-8&'
for page in range(start_page, end_page + 1):
    data = {'kw': ba_name, 'pn': (page - 1) * 50, }
    data = urllib.parse.urlencode(data)
    url_t = url + data
    print(url_t)
    request = urllib.request.Request(url=url_t, headers=headers)

    print('第%s页开始下载......' % page)

    response = urllib.request.urlopen(request)
    file_name = ba_name + '-' + str(page) + '.html'
    file_path = ba_name + '/' + file_name
    # 写内容
    with open(file_path, 'wb') as fp:
        fp.write(response.read())
    print('第%s页结束下载' % page)
