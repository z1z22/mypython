import requests
from lxml import etree
from inputdigit import inputdigit
import json

def handle_request(url, data):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
    r = requests.get(url, params=data, headers = headers)
    return r

# def get_info(content):
#     tree = etree.HTML(content)
#     div_ls = tree.xpath('//div[@class=movie-list-panel pictext]/div')
#     text_ls = []
#     # for div in div_ls:
#         dicts = {
#             'MOVNAME': div.xpath('//span[@class="movie-name-text"]/a/text()')[0],
#             'MOVHREF': div.xpath('//span[@class="movie-name-text"]/a/@href')[0],
#             'MOVCREW': div.xpath('//div[@class="movie-crew"]/text()')[0],
#             'MOVMISC': div.xpath('//div[@class="cmovie-misc"]/text()')[0],
#             'RATINGNUM': div.xpath('//span[@class="rating_num"/text]')[0],
#             'COMMENTNUM': div.xpath('//span[@class="comment-num""/text]')[0],
#         }
#         print(dicts)
#         text_ls.append(dicts)
#     return text_ls


def main():
    url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&'
    page = inputdigit('请输入页码:')
    number= inputdigit('输入每页显示数量:')
    data = {
        'start': (page - 1)*number,
	    'limit': number,
    }
    r = handle_request(url, data)
    # print (r.json())
    # exit()
    # text_ls = get_info(r.text)

    string = json.dumps(r.json(), ensure_ascii = False)
    # print (type(string))
    with open('douban.json', 'w') as fp:
        fp.write(string)




if __name__ == "__main__":
    main()
