from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://http://www.ebrun.com/20170703/236949.shtml')

bs_obj = BeautifulSoup(html.read(),"html.parser")
text_list = bs_obj.find_all("a","g-top-bar-nav")
for text in text_list:
	print(text.get_text())
html.close()

