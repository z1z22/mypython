import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=6&interval_id=100%3A90&action=&'
data = {
    'start':(page - 1)*number,
    'limit': number,
}

query_string = urllib.parse.urlencode(data)

print(query_string)