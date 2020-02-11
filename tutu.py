import urllib.request
import urllib.parse

url = 'http://p.9rti.net/uploadfile/2014/0729/10/0.jpg'
with open('meituurl.txt', 'a') as fp:
	for n in range(1,25):
		full_url = url + str(n)+ '.jpg\n'
		fp.write(full_url)


#http://p.9rti.net/uploadfile/2014/0725/11/021.jpg
# http://p.9rti.net/uploadfile/2014/0729/09/036.jpg
# http://p.9rti.net/uploadfile/2014/0728/10/034.jpg
# http://p.9rti.net/uploadfile/2014/0725/11/02.jpg
# http://p.9rti.net/uploadfile/2014/0729/10/024.jpg