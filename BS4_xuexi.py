import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
#url = "http://www.renren.com/307444178/profile"
'''url = 'http://www.renren.com/307444178'
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 'Cookie': 'anonymid=jrjb91uy-3ai5j1; depovince=ZGQT; jebecookies=617c346b-ba55-4cd1-99ce-2aad5e1194bf|||||; _r01_=1; JSESSIONID=abcHfgKGfRIavdOD-pFIw; ick_login=58432d4c-bce2-45d5-a613-1060c3c87a8e; _de=98655789833E2A3EE045A6D35FC0CCA2; p=903e1f3137204b4f47efd0710c6824888; first_login_flag=1; ln_uact=z1z22@tom.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20160726/1955/h_main_1QuS_fd9c000512f4195a.jpg; t=8a2e7d77ead1e2848ce4af0b97e0399c8; societyguester=8a2e7d77ead1e2848ce4af0b97e0399c8; id=307444178; xnsid=60bf900f; ver=7.0; loginfrom=null; jebe_key=2fe493a3-61f9-4c6d-afe6-94a412f584e1%7Cbcb3fd69f0cb3214307c2b19585a5911%7C1548860030106%7C1%7C1548860030147; wp_fold=0; XNESSESSIONID=e3820269b92e; WebOnLineNotice_307444178=1'
}

request = urllib.request.Request(url = url,headers = headers)
response = urllib.request.urlopen(request)

with open('renren_home.html','wb') as fp:
	fp.write(response.read())'''
soup = BeautifulSoup(open('renren_home.html'),'lxml')
#print(soup.a)#soup.a只能找到第一个符合条件的标签
#获取属性
#print(soup.a['title'])
#print(soup.a['href'])
#print(soup.a['target'])
#print(soup.a.attrs)#获取全部属性,生成字典
#获取内容
#print(soup.div.get_text())
#print(soup.a.string)
#print(soup.a.get_text())
#print(soup.find('a',title = 'xxx'))#只找到第一个
#print(soup.find('a',class_ = 'xxx'))#找到所有a
#print(soup.find_all('a'),alt = 'xxx')#找到所有a
#print(soup.find_all('a'),id = 'xxx')#找到所有a

#div = soup.find('a',id = 'xxx')
#div.find(div,id='xxx')

#with open('bs_renren_home.html','wb') as fp:
#	fp.write(soup.decode('utf-8'))



