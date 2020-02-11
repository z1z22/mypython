# import requests
# import inputdigit
# from bs4 import BeautifulSoup
# from lxml import etree
# import os
# import time
# import re
# import retrying
# import pymongo


# def handler_request(url,page = None):
# 	if page is None:
# 		url = url
# 	else:
# 		url = url.format(page)
# 	headers = {
# 	        'User-Agent': 'Mozilla/5.0 (MacintoshIntel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
# 	        'Referer':'https://www.aisinei.org/'
# 	}
# 	# print(url)
# 	r = requests.get(url = url, headers = headers)
# 	return r

# def picture_list(content):
# 	piclist = []
# 	soup  = BeautifulSoup(content,'lxml')
# 	a_ls = soup.select('dt > a')
# 	for a in a_ls:
# 		print(a.text)
# 		print(a['href'])
# 		title_dict = {'title': a.text,'href': a['href']}
# 		piclist.append(title_dict)
# 	return piclist

# def total_page(text):
# 	pattern = re.compile(r'<span.*?(.*?).*?</span>') 
# 	t_page = pattern.findall(text)
# 	# tree = etree.HTML(text)
# 	# t_page = tree.xpath('//label')
# 	# print(t_page)
# 	return t_page
# # //*[@id="moderate"]/div[1]/div/label/span
# # <span title="共 () 页"> / 21 页</span>
# def main():

# 	url = 'https://www.aisinei.org/'
# 	r = handler_request(url)
# 	pics_list = picture_list(r.text)
# 	num = 1
# 	for pics in pics_list:
# 		print(pics['title'] + '----' + str(num))
# 		num += 1
# 	pp = 1#inputdigit.inputdigit('Title number: ')
# 	title_url = pics_list[pp-1]['href']
# 	title = pics_list[pp-1]['title']

# 	r = handler_request(title_url)
# 	t_page = total_page(r.text)
# 	print(t_page)


# 	# print('You will download ' + title + ' ' + t_page)





# if __name__ == '__main__':
# 	main()
# # n = 30
# # href = 'fdsa'
# # print('No.{}: {} is completed.'.format(n, href))
# # <a href="https://www.aisinei.org/forum-beautyleg-135.html" class="last">... 135</a>

# # # <label><input type="text" name="custompage" class="px" size="2" title="输入页码，按回车快速跳转" value="1" onkeydown="if(event.keyCode==13) {window.location='forum.php?mod=forumdisplay&amp;fid=37&amp;page='+this.value;; doane(event);}"><span title="共 5 页"> / 5 页</span></label>

# for i in range(10):
# 	print (i)
# import requests
# headers = {
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
# }
# url = 'https://sou.zhaopin.com/?p=2&jl=北京&kw=python&kt=3'
# requests.get(url, headers = headers)
# r = requests.get(url, headers = headers)
# # print(r.text)

# l  = ['']
# print(l[0])

# x = [x**2 for x in range(1,101)]
# print(sum(x))
# jl = [x**2 for x in range(1,90,2)]

# kl = [x**2 for x in range(2,89,2)]
# print(sum(jl), sum(kl), sum(jl)-sum(kl))


# print(89*89)
# print(7921 - 4356)
# import time
# now = time.time()
# r = "\n\n    百年孤独\n\n\n    \n\n"
# print(r.strip('\n '))
# n  = []
# time.sleep(7)
# if  len(n): 
# 	print('FDSAF')
# else:
#  print('fdsaf')

# a = ' ...fds '
# print(a.strip('. '))
# end = time.time()
# print(int(end - now))
# use_time = 15
# print('All tasks completed.(time: {}m{}s)'.format(use_time//60,use_time%60))
# href = 'https://www.aisinei.com/aaa'
# if 'https://www.aisinei.com/thread-17325-1-2.html' in href:
# 	print('zai')
# else:
# 	print('buzai')
# href = 'aaa'
# if ('https://www.aisinei.com' in href) is False:
# 	href = 'https://www.aisinei.com'+ href
# print(href)
# a = 'aaa45678张'
# b = [s for s in a if s.isdigit()]
# print(''.join(b))

# b = ['a','b','c','d']
# print(';\n'.join(b))
# with open('1969 - Kat (10_26).txt','w') as fb:
# 	fb.write('fdafdafdsa')
# pic_item = 'jmrenti_scrapy/欧美人体艺术/1969 - Kat/1969 - Kat (10_26).jpg'

# dirpath = '/User/pyhton/pic/' + '/'.join(pic_item.split('/')[:-1]).replace(' ','')
# print(dirpath)
# a = "/company/bare-maidens/"
# print(a.split('/',2)[1])

# print(a.replace(' ','').replace('/','_'))

# n = 100
# pn = []
# for i in range(2,n):
#     for x in pn:
#         if i %x ==0:
#             break
#     else:
#         pn.append(i)
# print(pn)

# alt="aaaaaaa   bbbbb ccc"
# print(alt.split()[0])
# print(alt.split()[1])
a_list = list('aabbbccddddssssetttwllllll')
print(a_list)

list_b = {x: a_list.count(x) for x in set(a_list)}
print(list_b)

from collections import Counter
print(Counter(a_list))






