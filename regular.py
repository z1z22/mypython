import re
'''利用正则表达式判断是否是email地址'''
def is_valid_email(addr):
	re_mail = re.compile(r'^(\w{1,}\.)?(\w{1,})@(\w{1,})(\.com|\.cn)$',re.I)#re.IGNORECASE不区分大小写,可写成re.I
	if re_mail.match(addr):#match匹配,search找到第一个.findall找到所有
		print('is  a email-addr.')
	else:
		print('is not a email addr.')


is_valid_email('Z122@QQ.CN')

