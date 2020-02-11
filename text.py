# import urllib.request
# import urllib.parse
# import re
# import os
# import requests

# # image_src = 'https://i.meizitu.net/2019/01/05a02.jpg'
# # filepath = './meizi/05003.jpg'
# # # https://pic.qiushibaike.com/system/pictures/12151/121513841/medium/4V181RYB0NW8O1AM.jpg

# # myheaders =  [('Referer', 'https://www.mzitu.com'),
# # ('Upgrade-Insecure-Requests', '1'),
# # ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'),
# # ]
# # opener = urllib.request.build_opener()
# # opener.addheaders = myheaders
# # urllib.request.install_opener(opener)

# # # urllib.request.urlretrieve(image_src,filepath )

# # import re


# # content = '''<div class="section-content">
# # 				            <div class="copy-wrapper">
# # 				                <span class="eyebrow"><span class="violator violator-secondary">限时优惠</span></span>
				
# # 				                <h2 class="headline">折抵换购，iPhone&nbsp;X<span class="small-caps">R</span> 仅 <span class="nowrap">RMB&nbsp;183/月</span>起，或 <span class="nowrap">RMB 4399</span> 起；<br class="large-show medium-hide small-hide">iPhone&nbsp;X<span class="small-caps">S</span>&nbsp;仅 <span class="nowrap">RMB&nbsp;275/月</span>起，或 <span class="nowrap">RMB 6599</span> 起<sup>*</sup>。</h2>
# # # 				                <h3 class="subhead subhead1">前往附近的 Apple Store 零售店，把你手上的 iPhone 升级换购成一个新的，时机正好。</h3>
# # # 				                <div class="cta-links">
# # # 				                    <a href="/cn/giveback/" class="cta more" aria-label="进一步了解">进一步了解</a>
# # # 				                </div>
# # # 				            </div>
# # # 				        </div>'''
# # # pattern = re.compile(r'<div class="copy-wrapper">.*?RMB&nbsp;(.*?)</span>.*?</div>', re.S)
# # # lt = pattern.search(content)
# # # print(type(lt.group(1)))


# # url = 'guochan/123/'


# # if 'https://www.meitulu.com' in url:
# # # 	url = url
# # # else:
# # # 	url = 'http://www.meitulu.com/'+ url
# # # print(url)

# # # https://mtl.ttsqgs.com/images/img/16729/1.jpg


# # # https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16728/49.jpg

# # UnboundLocalEr = '''<li >
# # <a href = "https://www.meitulu.com/item/16784.html" target = "_blank" > <img src = "https://mtl.ttsqgs.com/images/img/16784/0.jpg" alt = "[Ugirls爱尤物] No.1317 小鹿 - 汹涌的小鹿[35]" width = "220" height = "300" original = "https://mtl.ttsqgs.com/images/img/16784/0.jpg" style = "display: inline;" > </a >
# # <p > 数量： 35 张 < /p >
# # <p > 机构： < a href = "https://www.meitulu.com/t/aiyouwu/" target = "_blank" class = "tags" > 爱尤物 < /a > </p >
# # <p > 模特：小鹿 < /p >

# # <p > 标签： < a href = "https://www.meitulu.com/t/juru/" target = "_blank" class = "tags" > 巨乳 < /a > <a href = "https://www.meitulu.com/t/nvshen/" target = "_blank" class = "tags" > 女神 < /a > <a href = "https://www.meitulu.com/t/baoru/" target = "_blank" class = "tags" > 爆乳 < /a > <a href = "https://www.meitulu.com/t/meixiong/" target = "_blank" class = "tags" > 美胸 < /a > </p >
# # <p class = "p_title" > <a href = "https://www.meitulu.com/item/16784.html" target = "_blank" > [Ugirls爱尤物] No.1317 小鹿 - 汹涌的小鹿 < /a > </p >
# # </li >'''


# # pattern = re.compile(r'<img src = "https://mtl.ttsqgs.com/images/img/(\d\d\d\d\d)/0.jpg".*?数量.*?(\d\d).*?张', re.S)

# # mo = pattern.findall(UnboundLocalEr)

# # print (mo)

# url_list = ['https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/1.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/2.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/3.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/4.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/5.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/6.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/7.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/8.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/9.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/10.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/11.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/12.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/13.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/14.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/15.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/16.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/17.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/18.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/19.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/20.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/21.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/22.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/23.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/24.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/25.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/26.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/27.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/28.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/29.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/30.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/31.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/32.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/33.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/34.jpg', 'https://www.meitulu.com/img.html?img=https://mtl.ttsqgs.com/images/img/16757/35.jpg', ]
# dirname = 'maieieei'
# n = 1
# for url in url_list:
#     filename = url.split("/")[-2] + '_' + url.split("/")[-1]
#     filepath = './meimeimei/'+filename
#     print(n)
#     myheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36')]
#     opener = urllib.request.build_opener()
#     opener.addheaders = myheaders
#     urllib.request.install_opener(opener)
#     urllib.request.urlretrieve(url, filepath)

#     # r = requests.get(url)
#     # with open(filepath, 'wb') as fs:
#     # 	fs.write(r.content)


#     # r = requests.get(url, stream=True)    
#     # with open('filepath', 'wb') as fs:
#     #     for chunk in r.iter_content(chunk_size=32):
#     #         fs.write(chunk)

#     n += 1

    
# Opera
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60
# Opera/8.0 (Windows NT 5.1; U; en)
# Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50
# Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50
 
# Firefox
# Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0
# Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10
 
# Safari
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2
 
# chrome
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36
# Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11
# Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16
 
# 360
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36
# Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko
 
 
# 淘宝浏览器
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11
 
# 猎豹浏览器
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER
# Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) 
# Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)"
# QQ浏览器
# Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)
# Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)
# sogou浏览器
# Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0
# Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)
# maxthon浏览器
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36

import inputdigit

            

a = inputdigit.inputdigit('fd:')
print(a)




