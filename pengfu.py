import requests
import time
import json
from lxml import etree

def handle_request(url, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (MacintoshIntel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
    }
    url = url %page
    # print(url)
    r = requests.get(url=url, headers=headers)
    return r

def parse_content(content,item_ls):

    tree = etree.HTML(content) #生成对象
    #抓取内容
    div_list = tree.xpath('//div[@class="list-item bg1 b1 boxshadow"]')
    # print(div_list)
    # print(len(div_list))
    for odiv in div_list:
        #获取标题
        title = odiv.xpath('.//h1/a/text()')[0]
        text_lt = odiv.xpath('.//dl/dd/div[2]/text()')
        text = "\n".join(text_lt).replace('\t','')
        # print(title)
        item = {
            'title': title,
            'text': text
        }
        item_ls.append(item)
    return item_ls

def main():
    start_page = int(input('start page: '))
    end_page = int(input('end page:'))
    url = 'https://www.pengfue.com/xiaohua_%s.html'
    item_ls = []
    for page in range(start_page, end_page+1):
        r = handle_request(url, page)
        r.encoding = 'UTF-8'
        item_ls = parse_content(r.text,item_ls)
        # print (item_ls)
        print('第%s页正在下载......' %page)
        time.sleep(2)
    with open('pengfu.json','w') as fp:
        json.dump(item_ls, fp)




if __name__ == "__main__":
    main()
